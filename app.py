# app.py
from flask import Flask
from config import Config
from extensions import db
from routes import register_routes
from flask_cors import CORS
from dotenv import load_dotenv
from seed_data import seed_data

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, supports_credentials=True, origins="*")
    db.init_app(app)
    register_routes(app)

    with app.app_context():
        db.create_all()
        seed_data()

    return app

app = create_app()
