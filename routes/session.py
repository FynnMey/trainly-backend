from flask import Blueprint, jsonify, request
from models import Session, Plan, PlanExercise, SessionExercise, SessionSet, Exercise
from utils.security import require_auth
from extensions import db
import datetime

session_bp = Blueprint("session_route", __name__)


def get_active_session(user_id):
    return db.session.query(Session).filter(
        (Session.user_id == user_id) & (Session.finished_at.is_(None))
    ).first()


def get_plan(plan_id):
    return db.session.query(Plan).filter_by(id=plan_id).first()


def get_previous_sets(exercise_id, limit):
    return (
        db.session.query(SessionSet)
        .join(SessionExercise)
        .filter(SessionExercise.exercise_id == exercise_id)
        .order_by(SessionSet.timestamp.desc())
        .limit(limit)
        .all()[::-1]
    )


@session_bp.route("/session-finish", methods=["POST"])
@require_auth
def session_finish():
    data = request.get_json()
    session_id = data.get("sessionId")

    if not session_id:
        return jsonify({"error": "Missing sessionId"}), 400

    session = db.session.query(Session).filter_by(id=session_id).first()
    if not session:
        return jsonify({"error": "Session not found"}), 404

    session.finished_at = datetime.datetime.now()
    db.session.commit()

    return jsonify({"message": "Session finished successfully."}), 200


@session_bp.route("/set-session", methods=["POST"])
@require_auth
def set_session():
    data = request.get_json()
    user_id = data.get("userId")
    plan_id = data.get("planId")

    if user_id is None or plan_id is None:
        return jsonify({"error": "Missing userId or planId"}), 400

    if get_active_session(user_id):
        return jsonify({"error": "You already have an active session."}), 400

    plan = get_plan(plan_id)
    if not plan:
        return jsonify({"error": "Plan not found"}), 404

    session = Session(
        user_id=user_id,
        plan_id=plan_id,
        started_at=datetime.datetime.now(),
        finished_at=None,
        is_synced=False,
    )
    db.session.add(session)
    db.session.flush()

    plan_exercises = db.session.query(PlanExercise).filter_by(plan_id=plan.id).all()

    for pe in plan_exercises:
        session_exercise = SessionExercise(
            session_id=session.id,
            exercise_id=pe.exercise_id,
            order=pe.order,
        )
        db.session.add(session_exercise)
        db.session.flush()

        previous_sets = get_previous_sets(pe.exercise_id, pe.sets)

        for i in range(pe.sets):
            last_weight = previous_sets[i].weight if i < len(previous_sets) else 0
            last_reps = previous_sets[i].reps if i < len(previous_sets) else 10

            session_set = SessionSet(
                session_exercise_id=session_exercise.id,
                weight=last_weight,
                reps=last_reps,
                timestamp=datetime.datetime.now(),
            )
            db.session.add(session_set)

    db.session.commit()

    return jsonify({"success": True, "sessionId": session.id}), 201


@session_bp.route("/session", methods=["POST"])
@require_auth
def get_session():
    data = request.get_json()
    user_id = data.get("userId")

    if user_id is None:
        return jsonify({"error": "Missing userId"}), 400

    session = get_active_session(user_id)
    if not session:
        return jsonify({"session": False}), 200


    session_exercises = db.session.query(SessionExercise).filter_by(session_id=session.id).all()
    exercises_data = []

    for se in session_exercises:
        exercise = db.session.query(Exercise).filter_by(id=se.exercise_id).first()
        sets = db.session.query(SessionSet).filter_by(session_exercise_id=se.id).all()

        sets_data = [
            {
                "id": s.id,
                "weight": s.weight,
                "reps": s.reps,
                "done": s.done,
                "timestamp": s.timestamp.isoformat(),
            }
            for s in sets
        ]

        exercises_data.append({
            "id": se.id,
            "exerciseId": se.exercise_id,
            "order": se.order,
            "name": exercise.name if exercise else "Unknown",
            "imageUrl": exercise.image_url if exercise else "",
            "sets": sets_data,
        })

    session_data = {
        "id": session.id,
        "userId": session.user_id,
        "planId": session.plan_id,
        "started_at": session.started_at.isoformat(),
        "exercises": exercises_data,
    }

    return jsonify({"session": session_data}), 200
