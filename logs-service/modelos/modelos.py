from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    experiencia = db.Column(db.String(60))
    telefono = db.Column(db.String(60))
