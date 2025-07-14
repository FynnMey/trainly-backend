from flask import Blueprint, request, jsonify, current_app

from models import User
from extensions import db
import jwt
import datetime

from utils.security import require_auth

auth_bp = Blueprint("auth_route", __name__)

@auth_bp.route("/secure", methods=["GET"])
@require_auth
def secure():
    return jsonify({"message": "Erfolgreich authentifiziert"})


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(account=data["account"]).first():
        return jsonify({"error": "account already registered"}), 400

    user = User(name=data["name"], account=data["account"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created", "user": { "id": user.id, 'account': user.name }}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    account = data.get("account")
    password = data.get("password")
    device_id = data.get("device_id")

    if not account or not password:
        return jsonify({"error": "Missing fields"}), 400


    user = User.query.filter_by(account=account).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    User.set_device_id(user, device_id)
    db.session.commit()

    payload = {
        "sub": str(user.id),
        "account": user.account,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30),
        "device_id": device_id or "unknown"
    }

    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({
        "status": 200,
        "message": "Login successful",
        "user": {"id": user.id, "account": user.account},
        "device_token": token
    })
