import os
import google.generativeai as genai

from flask import Blueprint, jsonify, request
from models import Exercise, Plan, PlanExercise
from utils.security import require_auth
from extensions import db

plans_bp = Blueprint("plans_route", __name__)


@plans_bp.route("/plans", methods=["POST"])
@require_auth
def plans_list():
    data = request.get_json() or {}
    user_id = data.get("userId")

    if user_id is None:
        return jsonify({"success": False, "message": "userId is required"}), 400

    plans = db.session.query(Plan.id, Plan.name).filter_by(user_id=user_id).all()

    plan_list = [
        {
            "id": plan.id,
            "name": plan.name,
        } for plan in plans
    ]

    return jsonify({"success": True, "plans": plan_list}), 200


@plans_bp.route("/plan", methods=["POST"])
@require_auth
def get_plan_by_id():
    data = request.get_json()
    plan_id = data.get("plan_id")

    if plan_id is None:
        return jsonify({"error": "Missing plan_id"}), 400

    plan = db.session.query(Plan).filter_by(id=plan_id).first()
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

    return jsonify({
        "plan": {
            "id": plan.id,
            "userId": plan.user_id,
            "name": plan.name,
            "description": plan.description,
            "exercises": exercises
        }
    })


@plans_bp.route("/plan/create", methods=["POST"])
@require_auth
def create_plan_with_exercises():
    data = request.get_json()

    required_fields = ["user_id", "name", "description"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required plan fields"}), 400

    new_plan = Plan(
        user_id=data["user_id"],
        name=data["name"],
        description=data["description"],
    )
    db.session.add(new_plan)
    db.session.flush()

    exercises = data.get("exercises", [])

    for e in exercises:
        if "exercise_id" not in e:
            continue

        plan_exercise = PlanExercise(
            plan_id=new_plan.id,
            exercise_id=e["exercise_id"],
            order=e.get("order", 1),
            sets=e.get("sets", 4),
            rest_time=e.get("rest_time", 60),
        )
        db.session.add(plan_exercise)

    db.session.commit()

    return jsonify({"success": True, "plan_id": new_plan.id}), 201


@plans_bp.route("/plan-ai/create", methods=["POST"])
def create_plan_with_ai():
    data = request.get_json()

    GENAI_API_KEY = os.getenv("GENAI_API_KEY")
    genai.configure(api_key=GENAI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

    results = db.session.query(
        Exercise.id,
        Exercise.name,
        Exercise.description,
        Exercise.muscle_groups,
    ).all()

    response_exers = [
        {
            "id": r[0],
            "name": r[1],
            "description": r[2],
            "muscle_groups": r[3],
        } for r in results
    ]

    # Muskelgruppen vom Nutzer (für Testzwecke hier hartkodiert, später aus data)
    user_muscle_groups = data.get("muscle_groups", "chest, back, legs")

    prompt = f"""
You are an expert fitness coach. Based on the list of all possible exercises and the user's important muscle groups, create a 3-day muscle-building workout plan.

- Use only exercises that target the user's specified muscle groups: {user_muscle_groups}
- Distribute the exercises logically over 3 training days, focusing on different muscle groups each day.
- Each exercise should include: id, name, sets (3-5), reps (8-12), rest_seconds (60-90).
- Return ONLY a JSON object, no extra explanation or text.

Format the output exactly like this:

{{
  "workout_plan": [
    {{
      "day": "Day 1",
      "muscle_groups": ["list of muscle groups"],
      "exercises": [
        {{
          "id": int,
          "name": string,
          "sets": int,
          "reps": int,
          "rest_seconds": int
        }},
        ...
      ]
    }},
    ...
  ]
}}

Here are the available exercises with details:

{response_exers}
"""

    response = model.generate_content(prompt)

    print(response.text)

    return jsonify({"success": True, "response": response.text}), 201
