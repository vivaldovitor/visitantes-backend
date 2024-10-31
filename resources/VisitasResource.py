from datetime import datetime
from flask_restful import Resource, marshal, reqparse
from models.Visitas import Visitas, visitasFields
from helpers.database import db
from sqlalchemy.exc import IntegrityError


parse = reqparse.RequestParser()
parse.add_argument('data', type=str, help='Problema na data')

class VisitasResource(Resource):
    def get(self):
        visita = Visitas.query.all()
        return {'visitas': marshal(visita, visitasFields)}
    
    def post(self):
        args = parse.parse_args()
        data = args['data']

        try:
            data_visita = datetime.strptime(data_visita, '%Y-%m-%d')
        except ValueError:
            return {'message': 'Formato de data de visita inválido. Use YYYY-MM-DD'}, 400

        try:
            visita = Visitas(data=data) 

            db.session.add(visita)
            db.session.commit()
            return marshal(visita, visitasFields), 201
        
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Erro de integridade: problema no cadastro da visita'}, 400
        
        except Exception as e:
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500
        

class VisitaResource(Resource):
    def get(self, id):
        visita = Visitas.query.get(id)
        if not visita:
            return {'message': 'Visita não encontrada'}, 404
        return {'visita': marshal(visita, visitasFields)}, 200
    
    def delete(self, id):
        visita = Visitas.query.get(id)
        if not visita:
            return {'message': 'Visita não encontrada.'}, 404
        try:
            db.session.delete(visita)
            db.session.commit()
            return {'message': 'Visita deletada com sucesso'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500


