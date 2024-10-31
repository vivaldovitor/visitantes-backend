from flask_restful import Resource, reqparse, marshal
from models.Visitantes import Visitantes, visitantesFields
from helpers.database import db
from sqlalchemy.exc import IntegrityError
from datetime import datetime

parse = reqparse.RequestParser()
parse.add_argument('nome', type=str, help='Problema no nome do visitante')
parse.add_argument('cidade', type=str, help='Problema no local de origem')
parse.add_argument('igreja', type=str, help='Problema na igreja')
parse.add_argument('data_visita', type=str, help='Problema na data da visita')

class VisitantesResource(Resource):

    def get(self):
        visitantes = Visitantes.query.all()
        return {'visitantes': marshal(visitantes, visitantesFields)}, 200
    
    def post(self):
        args = parse.parse_args()
        nome = args['nome']
        cidade = args['cidade']
        igreja = args['igreja']
        data_visita = args['data_visita']

        try:
            data_visita = datetime.strptime(data_visita, '%Y-%m-%d')
        except ValueError:
            return {'message': 'Formato de data de visita inválido. Use YYYY-MM-DD'}, 400
        
        try:
            visitante = Visitantes(
                nome=nome,
                cidade=cidade,
                igreja=igreja,
                data_visita=data_visita
            )
        
            db.session.add(visitante)
            db.session.commit()
            return marshal(visitante, visitantesFields), 201
        
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Erro de integridade: problema no cadastro'}, 400
        except Exception as e:
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500


class VisitanteResource(Resource):

    def get(self, id):
        visitante = Visitantes.query.get(id)
        if not visitante:
            return {'Error': 'Visitante não encontrado'}, 404
        return {'visitante': marshal(visitante, visitantesFields)}, 200
    
    def put(self, id):
        args = parse.parse_args()
        visitante = Visitantes.query.get(id)
        if not visitante:
            return {'Error': 'Visitante não encontrado'}, 404
        

        try:
            if args.get('nome'):
                visitante.nome = args['nome']
            if args.get('cidade'):
                visitante.cidade = args['cidade']
            if args.get('igreja'):
                visitante.igreja = args['igreja']
            else:
                visitante.igreja = 'não crente'

            if args.get('data_visita'):
                try:
                    visitante.data_visita = datetime.strptime(args['data_visita'], '%Y-%m-%d')
                
                except ValueError:
                    return {'message': 'Formato de data de visita inválido. Use YYYY-MM-DD'}, 400
                
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

