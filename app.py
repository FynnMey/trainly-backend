from flask import Flask
from flask_admin import Admin

from config import Config
from extensions import db
from models import User, Plan, Exercise, PlanExercise
from routes import register_routes
from flask_cors import CORS
from dotenv import load_dotenv
from seed_data import seed_data
from flask_admin.contrib.sqla import ModelView

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)

CORS(app, supports_credentials=True, origins="*")
db.init_app(app)
register_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True, host="0.0.0.0")