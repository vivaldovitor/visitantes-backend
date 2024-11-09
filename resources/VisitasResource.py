from datetime import datetime
from flask_restful import Resource, reqparse, marshal
from models.Visitas import Visitas, visitasFields
from models.Visitantes import Visitantes
from helpers.database import db
from sqlalchemy.exc import IntegrityError
from helpers.logging.logger_config import get_logger

logger = get_logger(__name__)

class VisitasResource(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('data', type=str, required=True, help='Data é obrigatória e deve estar no formato YYYY-MM-DD')
        self.parse.add_argument('visitantes', type=list, location='json', help='Lista de visitantes deve ser uma lista de objetos JSON')

    def get(self, data=None):
        try:
            if data:
                try:    
                    data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
                except ValueError:
                    return {'message': 'Formato de data inválido. Use YYYY-MM-DD'}, 400
                visitas = Visitas.query.filter_by(data=data_formatada).all()
            else:
                visitas = Visitas.query.all()
            
            visitas_dict = [visita.to_dict() for visita in visitas]
            logger.info("Consulta realizada com sucesso!")
            return {'visitas': marshal(visitas_dict, visitasFields)}, 200
        except Exception as e:
            logger.error(f'Erro ao buscar visitas: {str(e)}')
            return {'message': 'Ocorreu um erro ao buscar visitas'}, 500


    def post(self):
        logger.info("Iniciando o cadastro de uma nova visita.")
        args = self.parse.parse_args()
        data_str = args['data']
        visitantes_data = args.get('visitantes', [])

        if not isinstance(visitantes_data, list):
            logger.error("Formato inválido: visitantes deve ser uma lista de objetos.")
            return {'message': 'Formato inválido: visitantes deve ser uma lista de objetos.'}, 400
        
        try:
            data = datetime.strptime(data_str, '%Y-%m-%d')
        except ValueError:
            logger.error("Formato de data inválido.")
            return {'message': 'Formato de data inválido. Use YYYY-MM-DD'}, 400

        visita = Visitas(data=data)
        db.session.add(visita)
        
        try:
            db.session.commit()
            logger.info("Visita criada com sucesso.")
        except IntegrityError as e:
            db.session.rollback()
            logger.error(f'Erro de integridade ao criar a visita: {str(e)}')
            return {'message': f'Erro de integridade ao criar a visita: {str(e)}'}, 400

        # Adicionando visitantes
        for visitante_info in visitantes_data:
            nome = visitante_info.get('nome')
            cidade = visitante_info.get('cidade')
            igreja = visitante_info.get('igreja')

            # Validação de nome
            if not nome:
                db.session.rollback()
                logger.error("Nome do visitante é obrigatório para cada visitante.")
                return {'message': 'Nome do visitante é obrigatório para cada visitante'}, 400
            
            visitante = Visitantes(
                nome=nome,
                cidade=cidade,
                igreja=igreja,
                visita_id=visita.visita_id
            )
            db.session.add(visitante)

        try:
            db.session.commit()
            logger.info("Visitantes adicionados com sucesso.")
            return marshal(visita, visitasFields), 201
        except IntegrityError:
            db.session.rollback()
            logger.error("Erro de integridade: problema no cadastro dos visitantes.")
            return {'message': 'Erro de integridade: problema no cadastro dos visitantes'}, 400
        except Exception as e:
            db.session.rollback()
            logger.error(f'Ocorreu um erro ao cadastrar visitantes: {str(e)}')
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500
            

class VisitaResource(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('data', type=str, required=True, help='Data é obrigatória e deve estar no formato YYYY-MM-DD')
        self.parse.add_argument('visitantes', type=list, location='json', help='Lista de visitantes deve ser uma lista de objetos JSON')

    def get(self, id):
        visita = Visitas.query.get(id)
        if not visita:
            return {'message': 'Visita não encontrada'}, 404
        logger.info("Consulta realizada com sucesso!")
        return {'visita': marshal(visita, visitasFields)}, 200
    
    def put(self, id):
        args = self.parse.parse_args()
        visita = Visitas.query.get(id)

        if not visita:
            return {'message': 'Visita não encontrada'}, 404

        # Atualizando a data da visita
        if args['data']:
            try:
                visita.data = datetime.strptime(args['data'], '%Y-%m-%d')
            except ValueError:
                return {'message': 'Formato de data inválido. Use YYYY-MM-DD'}, 400

        # Atualizando ou criando novos visitantes
        if args['visitantes']:
            visitantes_data = args['visitantes']
            for visitantes_info in visitantes_data:
                nome = visitantes_info.get('nome')
                cidade = visitantes_info.get('cidade')
                igreja = visitantes_info.get('igreja')

                if nome:
                    # Tentando encontrar o visitante já existente pela visita_id e nome
                    visitante = Visitantes.query.filter_by(visita_id=visita.visita_id, nome=nome).first()
                    
                    if visitante:
                        # Visitante encontrado, atualizar informações
                        visitante.cidade = cidade
                        visitante.igreja = igreja
                        logger.info(f'Visitante {nome} atualizado com sucesso.')
                    else:
                        # Visitante não encontrado, criar novo
                        visitante = Visitantes(
                            nome=nome,
                            cidade=cidade,
                            igreja=igreja,
                            visita_id=visita.visita_id
                        )
                        db.session.add(visitante)
                        logger.info(f'Visitante {nome} adicionado com sucesso.')

        try:
            db.session.commit()
            logger.info(f'Visita e/ou visitantes atualizados com sucesso! (ID: {id}).')
            return marshal(visita, visitasFields), 200
        except IntegrityError as e:
            db.session.rollback()
            logger.error(f'Erro de integridade ao atualizar a visita ou visitantes: {str(e)}')
            return {'message': f'Erro de integridade ao atualizar o visitante: {str(e)}'}, 400
        except Exception as e:
            db.session.rollback()
            logger.error(f'Ocorreu um erro ao atualizar visita: {str(e)}')
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500

    def delete(self, id):
        try:
            visita = Visitas.query.get(id)
            if not visita:
                return {'message': 'Visita não encontrada'}, 404
            
            db.session.delete(visita)
            db.session.commit()

            return {'message': 'Visita e visitantes associados foram deletados com sucesso'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Ocorreu um erro: {str(e)}'}, 500
