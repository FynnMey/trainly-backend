from flask import Blueprint, jsonify, request

from models import Session, Plan, PlanExercise, SessionExercise, SessionSet, Exercise
from utils.security import require_auth
from extensions import db
import datetime

session_bp = Blueprint("session_route", __name__)

@session_bp.route("/session-finish", methods=["POST"])
@require_auth
def session_finish():
    data = request.get_json()

    session_id = data.get("sessionId")

    session = db.session.query(Session).filter(Session.id == session_id).first()

    if session is None:
        return jsonify({"error": "Session set not found."}), 400

    session.finished_at = datetime.datetime.now()
    db.session.commit()

    return jsonify({"message": "Weight updated successfully"}), 200


@session_bp.route("/set-weight", methods=["POST"])
@require_auth
def session_set_weight():
    data = request.get_json()

    weight = data.get("weight")
    session_set_id = data.get("sessionSetId")

    if weight is None or session_set_id is None:
        return jsonify({"error": "Missing required fields: weight or sessionSetId"}), 400

    try:
        weight = float(weight)
    except (ValueError, TypeError):
        return jsonify({"error": "Please enter a valid number."}), 400

    session_set = db.session.query(SessionSet).filter(SessionSet.id == session_set_id).first()

    if session_set is None:
        return jsonify({"error": "Session set not found."}), 400

    session_set.weight = weight
    db.session.commit()

    return jsonify({"message": "Weight updated successfully"}), 200


@session_bp.route("/set-done", methods=["POST"])
@require_auth
def session_set_done():
    data = request.get_json()

    done = data.get("done")
    session_set_id = data.get("sessionSetId")

    print(done)

    if session_set_id is None or done is None:
        return jsonify({"error": "Missing required fields: reps and/or sessionSetId"}), 400

    try:
        done = bool(done)
    except (ValueError, TypeError):
        return jsonify({"error": "Please enter a valid number for reps."}), 400

    session_set = db.session.query(SessionSet).filter(SessionSet.id == session_set_id).first()

    if session_set is None:
        return jsonify({"error": "Session set not found."}), 400

    session_set.done = done
    db.session.commit()

    print(session_set.done)

    return jsonify({"message": "Reps updated successfully."}), 200


@session_bp.route("/set-reps", methods=["POST"])
@require_auth
def session_set_reps():
    data = request.get_json()

    reps = data.get("reps")
    session_set_id = data.get("sessionSetId")

    if session_set_id is None or reps is None:
        return jsonify({"error": "Missing required fields: reps and/or sessionSetId"}), 400

    try:
        reps = int(reps)
    except (ValueError, TypeError):
        return jsonify({"error": "Please enter a valid number for reps."}), 400

    session_set = db.session.query(SessionSet).filter(SessionSet.id == session_set_id).first()

    if session_set is None:
        return jsonify({"error": "Session set not found."}), 400

    session_set.reps = reps
    db.session.commit()

    return jsonify({"message": "Reps updated successfully."}), 200


@session_bp.route("/set-session", methods=["POST"])
@require_auth
def set_session():
    data = request.get_json()

    existing_session = db.session.query(Session).filter(
        (Session.user_id == data["userId"]) & (Session.finished_at.is_(None))
    ).first()

    print(existing_session)

    if existing_session:
        return jsonify({"error": "You already have an active session."}), 400

    plan = db.session.query(Plan).filter(Plan.id == data['planId']).first()
    if not plan:
        return jsonify({"error": "Plan not found"}), 404

    session = Session(
        user_id=data["userId"],
        plan_id=data["planId"],
        started_at=datetime.datetime.now(),
        finished_at=None,
        is_synced=False,
    )
    db.session.add(session)
    db.session.flush()

    plan_exercises = db.session.query(PlanExercise).filter(PlanExercise.plan_id == plan.id).all()

    for pe in plan_exercises:
        session_exercise = SessionExercise(
            session_id=session.id,
            exercise_id=pe.exercise_id,
            order=pe.order,
        )
        db.session.add(session_exercise)
        db.session.flush()

        last_sets = (
            db.session.query(SessionSet)
            .join(SessionExercise)
            .filter(SessionExercise.exercise_id == pe.exercise_id)
            .order_by(SessionSet.timestamp.desc())
            .limit(pe.sets)
            .all()[::-1]
        )

        for i in range(pe.sets):
            last_weight = last_sets[i].weight if i < len(last_sets) else 0
            last_reps = last_sets[i].reps if i < len(last_sets) else 10

            session_set = SessionSet(
                session_exercise_id=session_exercise.id,
                weight=last_weight,
                reps=last_reps,
                timestamp=datetime.datetime.now(),
            )
            db.session.add(session_set)

    db.session.commit()

    return jsonify({ "success": True, "sessionId": session.id })

@session_bp.route("/session", methods=["POST"])
@require_auth
def get_session():
    data = request.get_json()
    user_id = data["user_id"]

    print(user_id)

    if user_id is None:
        return jsonify({"error": "user_id is required"}), 400

    session = db.session.query(Session).filter(
        (Session.user_id == user_id) & (Session.finished_at.is_(None))
    ).first()

    if not session:
        return jsonify({ "session": False })

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
            "sets": sets_data
        })

    session_data = {
        "id": session.id,
        "userId": session.user_id,
        "planId": session.plan_id,
        "started_at": session.started_at.isoformat(),
        "exercises": exercises_data
    }

    return jsonify({ "session": session_data })
