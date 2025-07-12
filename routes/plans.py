from models import Exercise
from utils.security import require_auth
from flask import Blueprint, jsonify, request
from models.planExercise import PlanExercise
from models.plan import Plan
from extensions import db

plans_bp = Blueprint("plans_route", __name__)

@plans_bp.route("/plan", methods=["POST"])
@require_auth
def get_plan():
    data = request.get_json()

    plan = db.session.query(Plan).filter(
        (Plan.id == data['plan_id'])
    ).first()

    if not plan:
        return jsonify({"error": "Plan not found"}), 404

    plan_exercises = (
        db.session.query(PlanExercise, Exercise)
        .join(Exercise, Exercise.id == PlanExercise.exercise_id)
        .filter(PlanExercise.plan_id == plan.id)
        .all()
    )

    exercises = [
        {
            "id": pe.id,
            "exerciseId": pe.exercise_id,
            "name": ex.name,
            "imageUrl": ex.image_url,
            "order": pe.order,
            "sets": pe.sets,
            "restTime": pe.rest_time,
        }
        for pe, ex in plan_exercises
    ]

    exercises.sort(key=lambda e: e["order"])

    plan_dict = {
        "id": plan.id,
        "userId": plan.user_id,
        "name": plan.name,
        "description": plan.description,
        "exercises": exercises
    }

    return jsonify({"plan": plan_dict})


@plans_bp.route("/plans", methods=["POST"])
@require_auth
def get_exercises():
    data = request.get_json()

    plan = Plan(
        user_id=data["user_id"],
        name=data["name"],
        description=data["description"],
    )

    db.session.add(plan)
    db.session.commit()

    plan_id = plan.id

    exercises = data.get("exercises", [])

    for e in exercises:
        plan_exercise = PlanExercise(
            plan_id=plan_id,
            exercise_id=e["exercise_id"],
            order=e.get("order", 1),
            sets=e.get("sets", 4),
            rest_time=e.get("rest_time", 60),
        )
        db.session.add(plan_exercise)

    db.session.commit()

    return jsonify({"success": True, "plan_id": plan_id})