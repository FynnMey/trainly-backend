from extensions import db

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=True)
    started_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime, nullable=True)
    is_synced = db.Column(db.Boolean, default=False)
