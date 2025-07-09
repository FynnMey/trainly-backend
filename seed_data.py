import os
from models.user import User
from models.exercise import Exercise
from extensions import db
from dotenv import load_dotenv

load_dotenv()

def seed_data():
    if not User.query.first():
        admin = User(
            id=0,
            name="Admin",
            account="admin",
            password_hash="hashed_admin_password"
        )
        db.session.add(admin)
        db.session.commit()

    if not Exercise.query.first():
        exercises = [
            Exercise(
                name="Liegestütze",
                description="Körper in gerader Linie halten, Arme schulterbreit aufstellen, tief runter und kontrolliert hochdrücken. Rücken und Bauch anspannen.",
                image_url="/static/exercise/images/liegestuetze.webp",
                gif_url="/static/exercise/gifs/liegestuetze.gif",
                muscle_groups=["Brust", "Trizeps", "Schultern", "Rumpf"]
            ),
            Exercise(
                name="Kniebeugen",
                description="Füße schulterbreit, Rücken gerade. In die Hocke gehen, bis die Oberschenkel parallel zum Boden sind. Gewicht auf den Fersen lassen.",
                image_url="/static/exercise/images/kniebeuge.webp",
                gif_url="/static/exercise/gifs/kniebeuge.gif",
                muscle_groups=["Beine", "Gesäß", "Rumpf"]
            ),
            Exercise(
                name="Plank",
                description="Ellbogen unter den Schultern, Körper bildet eine gerade Linie. Bauch und Gesäß anspannen. Nicht durchhängen oder hochstrecken.",
                image_url="/static/exercise/images/plank.webp",
                gif_url="/static/exercise/gifs/plank.gif",
                muscle_groups=["Bauch", "Rücken", "Schultern"]
            ),
            Exercise(
                name="Crunches",
                description="Auf den Rücken legen, Knie anwinkeln, Hände hinter den Kopf. Oberkörper leicht nach oben rollen, nicht mit Schwung arbeiten.",
                image_url="/static/exercise/images/crunches.webp",
                gif_url="/static/exercise/gifs/crunches.gif",
                muscle_groups=["Bauch"]
            )
        ]

        db.session.add_all(exercises)
        db.session.commit()
