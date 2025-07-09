from models import Exercise
from utils.security import require_auth
from flask import Blueprint, jsonify
from extensions import db

exercise_bp = Blueprint("exercise_route", __name__)

@exercise_bp.route("/exercises", methods=["GET"])
@require_auth
def get_exercises():
    results = db.session.query(
        Exercise.id,
        Exercise.name,
        Exercise.image_url,
    ).all()

    response = [
        {
            "id": r[0],
            "name": r[1],
            "image_url": r[2]
        } for r in results
    ]

    print(response)

    return jsonify(response)