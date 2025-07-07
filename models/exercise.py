from extensions import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    gif_url = db.Column(db.String(255))
    muscle_groups = db.Column(db.JSON)
