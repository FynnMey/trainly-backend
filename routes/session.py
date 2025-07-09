from flask import Blueprint, jsonify, request

from models import Session
from utils.security import require_auth
from extensions import db

session_bp = Blueprint("session_route", __name__)

@session_bp.route("/set-session", methods=["POST"])
@require_auth
def set_session():
    data = request.get_json()

    session = db.session.query(Session).filter(
        (Session.user_id == data["userId"]) & (Session.finished_at.is_(None))
    ).first()

    if session:
        return jsonify({"error": "Cannot create a new session while an active session already exists."}), 404


    return jsonify({ True })
