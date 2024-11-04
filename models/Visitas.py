from flask_restful import fields
from helpers.database import db

visitasFields = {
    'visita_id': fields.Integer,
    'data': fields.DateTime,
    'visitantes': fields.List(fields.Nested({
        'visitante_id': fields.Integer,
        'nome': fields.String,
        'cidade': fields.String,
        'igreja': fields.String
    }))
}

class Visitas(db.Model):
    __tablename__ = 'visitas'

    visita_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False, unique=True)  

    visitantes = db.relationship('Visitantes', backref='visita', lazy=True)

    def to_dict(self):
        return {
            'visita_id': self.visita_id,
            'data': self.data,
            'visitantes': [v.to_dict() for v in self.visitantes]
        }

    def __repr__(self):
        return f'<Visita {self.visita_id} em {self.data}>'
