from flask_restful import fields
from helpers.database import db


visitasFields = {
    'id': fields.Integer,
    'data': fields.DateTime
}

class Visitas(db.Model):
    __tablename__ = 'visitas'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)

    visitantes = db.relationship('Visitantes', backref='visita', lazy=True)
