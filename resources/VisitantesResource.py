from flask_restful import Resource, reqparse, marshal
from models.Visitantes import Visitantes, visitantesFields
from helpers.database import db
from sqlalchemy.exc import IntegrityError
from datetime import datetime

class VisitantesResource(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('nome_visitante', type=str, help='Problema no nome do visitante')
        self.parser.add_argument('local_origem', type=str, help='Problema no local de origem')
        self.parser.add_argument('igreja', type=str, help='Problema na igreja')
        self.parser.add_argument('data_visita', type=str, help='Problema na data da visita')

    def get(self):
        visitantes = Visitantes.query.all()
        return {'visitantes': marshal(visitantes, visitantesFields)}, 200

    def post(self):
        args = self.parser.parse_args()
        nome_visitante = args['nome_visitante']
        local_origem = args['local_origem']
        igreja = args['igreja']
        data_visita = args['data_visita']

        try:
            data_visita = datetime.strptime(data_visita, '%Y-%m-%d')
        except ValueError:
            return {'message': 'Formato de data de visita inválido. Use YYYY-MM-DD'}, 400

        try:
            if not igreja:
                igreja = 'não crente'

            visitante = Visitantes(
                nome_visitante=nome_visitante,
                local_origem=local_origem,
                igreja=igreja,
                data_visita=data_visita
            )

            db.session.add(visitante)
            db.session.commit()

            return marshal(visitante, visitantesFields), 201
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Erro de integridade: problema no cadastro.'}, 400
        except Exception as e:
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500

class VisitanteResource(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('nome_visitante', type=str, help='Problema no nome do visitante')
        self.parser.add_argument('local_origem', type=str, help='Problema no local de origem')
        self.parser.add_argument('igreja', type=str, help='Problema na igreja')
        self.parser.add_argument('data_visita', type=str, help='Problema na data da visita')

    def get(self, id):
        visitantes = Visitantes.query.get(id)
        if not visitantes:
            return {"Error": "Visitante não encontrado"}, 404
        return {'visitantes': marshal(visitantes, visitantesFields)}, 200


    def put(self, id):
        args = self.parser.parse_args()
        visitante = Visitantes.query.get(id)
        if not visitante:
            return {'message': 'Visitante não encontrado.'}, 404

        try:
            # Verificar se o nome foi fornecido e não é vazio
            if args.get('nome_visitante'):
                visitante.nome_visitante = args['nome_visitante']
            if args.get('local_origem'):
                visitante.local_origem = args['local_origem']

            # Verificar se a data de visita foi fornecida e está no formato correto
            if args.get('data_visita'):
                try:
                    visitante.data_visita = datetime.strptime(args['data_visita'], '%Y-%m-%d')
                except ValueError:
                    return {'message': 'Formato de data de visita inválido. Use YYYY-MM-DD'}, 400

            if args.get('igreja'):
                visitante.igreja = args['igreja']
            else:
                visitante.igreja = 'não crente'

            db.session.commit()
            return marshal(visitante, visitantesFields), 200
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Erro de integridade: problema no cadastro.'}, 400
        except Exception as e:
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500


    def delete(self, id):
        visitante = Visitantes.query.get(id)
        if not visitante:
            return {'message': 'Visitante não encontrado.'}, 404

        try:
            db.session.delete(visitante)
            db.session.commit()
            return {'message': 'Visitante deletado com sucesso!'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500
