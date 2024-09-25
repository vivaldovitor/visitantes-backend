from flask_restful import fields
from helpers.database import db
from datetime import datetime

visitantesFields = {
    'id': fields.Integer,
    'nome_visitante': fields.String,
    'local_origem': fields.String,
    'igreja': fields.String,
    'data_visita': fields.DateTime
}

class Visitantes(db.Model):
    __tablename__ = 'visitantes'
    id = db.Column(db.Integer, primary_key=True)
    nome_visitante = db.Column(db.String(100), nullable=False)
    local_origem = db.Column(db.String(100), nullable=True)
    igreja = db.Column(db.String(100), nullable=True)  
    data_visita = db.Column(db.DateTime, nullable=False)


    def __repr__(self):
        return f'<Visitante {self.nome_visitante}>'
