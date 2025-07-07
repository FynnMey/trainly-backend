from extensions import db

class SessionSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_exercise_id = db.Column(db.Integer, db.ForeignKey('sessionexercise.id'))
    weight = db.Column(db.Float)
    reps = db.Column(db.Integer)
    done = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime)
