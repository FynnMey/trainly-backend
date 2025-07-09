from .auth import auth_bp
from .exercise import exercise_bp
from .plans import plans_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(exercise_bp)
    app.register_blueprint(plans_bp)
