from flask_restful import Api
from resources.IndexResource import IndexResource
from resources.VisitasResource import VisitasResource, VisitaResource
from resources.VisitantesResource import VisitantesResource, VisitanteResource

api = Api()

# Index
api.add_resource(IndexResource, '/')

# Visitas
api.add_resource(VisitaResource, '/visitas/<int:id>')
api.add_resource(VisitasResource, '/visitas', '/visitas/<string:data>')

# Visitantes
api.add_resource(VisitantesResource, '/visitantes')
api.add_resource(VisitanteResource, '/visitantes/<int:id>')

