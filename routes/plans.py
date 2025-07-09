from utils.security import require_auth
from flask import Blueprint, jsonify, request
from models.planExercise import PlanExercise
from models.plan import Plan
from extensions import db


plans_bp = Blueprint("plans_route", __name__)

@plans_bp.route("/plans", methods=["POST"])
@require_auth
def get_exercises():
    data = request.get_json()

    print(data)

    plan = Plan(
        user_id=data["user_id"],
        name=data["name"],
        description=data["description"],
    )

    db.session.add(plan)
    db.session.commit()

    plan_id = plan.id

    exercises = data.get("exercises", [])

    print(exercises)

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