from flask_restful import Resource, marshal, reqparse
from models.Visitantes import Visitantes, visitantesFields
from helpers.database import db
from sqlalchemy.exc import IntegrityError

class VisitantesResource(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('visita_id', type=int, required=True, help='ID da visita é obrigatório')
        self.parse.add_argument('nome', type=str, required=True, help="Nome do visitante é obrigatório")
        self.parse.add_argument('cidade', type=str, help="Cidade do visitante")
        self.parse.add_argument('igreja', type=str, help="Igreja do visitante")

    def get(self):
        visitantes = Visitantes.query.all()
        print(f"Retornando {visitantes} visitantes.")
        return {'visitantes': marshal(visitantes, visitantesFields)}, 200
    
    def post(self):
        args = self.parse.parse_args()
        visitante = Visitantes(
            visita_id=args['visita_id'],
            nome=args['nome'],
            cidade=args.get('cidade'),
            igreja=args.get('igreja')
        )

        db.session.add(visitante)
        try:
            db.session.commit()
            return marshal(visitante, visitantesFields), 201
        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Erro de integridade ao criar o visitante'}, 400 
        except Exception as e:
            db.session.rollback()
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500


class VisitanteResource(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('visita_id', type=int, help='ID da visita')
        self.parse.add_argument('nome', type=str, help="Nome do visitante")
        self.parse.add_argument('cidade', type=str, help="Cidade do visitante")
        self.parse.add_argument('igreja', type=str, help="Igreja do visitante")

    def get(self, id):
        visitante = Visitantes.query.get(id)
        if not visitante:
            return {'message': 'Visitante não encontrado'}, 404
        return {'visitante': marshal(visitante, visitantesFields)}, 200

    def put(self, id):
        args = self.parse.parse_args()
        visitante = Visitantes.query.get(id)
        if not visitante:
            return {'message': 'Visitante não encontrado'}, 404

        if args['visita_id'] is not None:
            visitante.visita_id = args['visita_id']
        if args['nome'] is not None:
            visitante.nome = args['nome']
        if args['cidade'] is not None:
            visitante.cidade = args['cidade']
        if args['igreja'] is not None:
            visitante.igreja = args['igreja']

        try:
            db.session.commit()
            return marshal(visitante, visitantesFields), 200
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Erro de integridade ao atualizar o visitante'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500

    def delete(self, id):
        visitante = Visitantes.query.get(id)
        if not visitante:
            return {'message': 'Visitante não encontrado'}, 404

        try:
            db.session.delete(visitante)
            db.session.commit()
            return {'message': 'Visitante deletado com sucesso'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500
