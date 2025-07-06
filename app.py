from flask import Flask
from config import Config
from extensions import db
from routes import register_routes
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)

CORS(app, supports_credentials=True, origins="*")
db.init_app(app)
register_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")
