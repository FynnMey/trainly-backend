from .auth import auth_bp
from .exercise import exercise_bp
from .plans import plans_bp
from .session import session_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(exercise_bp)
    app.register_blueprint(plans_bp)
    app.register_blueprint(session_bp)
