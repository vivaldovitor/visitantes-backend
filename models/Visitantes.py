from flask_restful import fields
from helpers.database import db

visitantesFields = {
    'visitante_id': fields.Integer,
    'visita_id': fields.Integer,
    'nome': fields.String,
    'cidade': fields.String,
    'igreja': fields.String,
}

class Visitantes(db.Model):
    __tablename__ = 'visitantes'

    visitante_id = db.Column(db.Integer, primary_key=True)
    visita_id = db.Column(db.Integer, db.ForeignKey('visitas.visita_id'), nullable=False)
    nome = db.Column(db.String, nullable=False)
    cidade = db.Column(db.String)
    igreja = db.Column(db.String)

    def to_dict(self):
        return {
            'visitante_id': self.visitante_id,
            'visita_id': self.visita_id,
            'nome': self.nome,
            'cidade': self.cidade,
            'igreja': self.igreja
        }

