import hmac
import hashlib
import os
import jwt
from models import User
from functools import wraps
from flask import request, jsonify

def generate_device_token(device_id: str, user_id: str, secret: str):
    message = f"{device_id}:{user_id}".encode()
    return hmac.new(secret.encode(), message, hashlib.sha256).hexdigest()


def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("token")
        if not token:
            return jsonify({"error": "Token fehlt"}), 401

        try:
            decoded = jwt.decode(
                token,
                os.getenv("SECRET_KEY"),
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token abgelaufen"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Ungültiger Token"}), 401

        try:
            user_id = int(decoded.get("sub"))
        except (TypeError, ValueError):
            return jsonify({"error": "Ungültige Benutzer-ID"}), 401

        db_user = User.query.get(user_id)
        if not db_user:
            return jsonify({"error": "Benutzer nicht gefunden"}), 401

        if (
            decoded.get("account") != db_user.account or
            decoded.get("device_id") != db_user.device_id or
            decoded.get("token") != db_user.auth_token
        ):
            return jsonify({"error": "Geräteauthentifizierung fehlgeschlagen"}), 403

        request.user = db_user
        return f(*args, **kwargs)

    return decorated_function