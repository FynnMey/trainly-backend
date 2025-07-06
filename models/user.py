from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    account = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))
    auth_token = db.Column(db.String(128))
    device_id = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_device_id(self, device_id):
        self.device_id = device_id

    def set_auth_token(self, auth_token):
        self.auth_token = auth_token