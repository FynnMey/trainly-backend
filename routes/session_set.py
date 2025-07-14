from flask import Blueprint, jsonify, request
from models import SessionSet
from utils.security import require_auth
from extensions import db

session_set_bp = Blueprint("session_set_route", __name__)

def get_session_set(session_set_id):
    if session_set_id is None:
        return None, jsonify({"error": "Missing required field: sessionSetId"}), 400

    session_set = db.session.query(SessionSet).filter_by(id=session_set_id).first()
    if session_set is None:
        return None, jsonify({"error": "Session set not found."}), 404

    return session_set, None, None


@session_set_bp.route("/set-weight", methods=["POST"])
@require_auth
def session_set_weight():
    data = request.get_json()
    weight = data.get("weight")
    session_set_id = data.get("sessionSetId")

    try:
        weight = float(weight)
    except (ValueError, TypeError):
        return jsonify({"error": "Please enter a valid number for weight."}), 400

    session_set, error_response, status = get_session_set(session_set_id)
    if error_response:
        return error_response, status

    session_set.weight = weight
    db.session.commit()

    return jsonify({"message": "Weight updated successfully."}), 200


@session_set_bp.route("/set-reps", methods=["POST"])
@require_auth
def session_set_reps():
    data = request.get_json()
    reps = data.get("reps")
    session_set_id = data.get("sessionSetId")

    try:
        reps = int(reps)
    except (ValueError, TypeError):
        return jsonify({"error": "Please enter a valid number for reps."}), 400

    session_set, error_response, status = get_session_set(session_set_id)
    if error_response:
        return error_response, status

    session_set.reps = reps
    db.session.commit()

    return jsonify({"message": "Reps updated successfully."}), 200


@session_set_bp.route("/set-done", methods=["POST"])
@require_auth
def session_set_done():
    data = request.get_json()
    done = data.get("done")
    session_set_id = data.get("sessionSetId")

    if done is None:
        return jsonify({"error": "Missing required field: done"}), 400

    session_set, error_response, status = get_session_set(session_set_id)
    if error_response:
        return error_response, status

    session_set.done = bool(done)
    db.session.commit()

    return jsonify({"message": "Set marked as done."}), 200


@session_set_bp.route("/set-delete", methods=["POST"])
@require_auth
def session_set_delete():
    data = request.get_json()
    session_set_id = data.get("sessionSetId")

    if session_set_id is None:
        return jsonify({"error": "Missing required field: sessionSetId"}), 400

    session_set = db.session.query(SessionSet).filter_by(id=session_set_id).first()
    if session_set is None:
        return jsonify({"error": "Session set not found."}), 404

    db.session.delete(session_set)
    db.session.commit()

    return jsonify({"message": "Session set deleted successfully."}), 200
