from extensions import db

class PlanExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    order = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    rest_time = db.Column(db.Integer)
