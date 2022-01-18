from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    image = db.Column(db.String())
    ability = db.Column(db.String(200), nullable=False, lazy=True)
    def __init__(self, id, name, image, ability):
        self.id = id
        self.name = name
        self.image = image
        self.ability = ability











