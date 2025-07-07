from extensions import db

class SessionExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    order = db.Column(db.Integer)
    skipped = db.Column(db.Boolean, default=False)
