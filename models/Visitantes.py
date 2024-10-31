from flask_restful import fields
from helpers.database import db

visitantesFields = {
    'id': fields.Integer,
    'visita_id': fields.Integer,
    'nome': fields.String,
    'cidade': fields.String,
    'igreja': fields.String,
}

class Visitantes(db.Model):
    __tablename__ = 'visitantes'
    id = db.Column(db.Integer, primary_key=True)
    visita_id = db.Column(db.Integer, db.ForeignKey('visitantes.id'), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=True)
    igreja = db.Column(db.String(100), nullable=True)  


    def __repr__(self):
        return f'<Visitante {self.nome}>'
