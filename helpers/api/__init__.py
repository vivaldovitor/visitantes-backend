from flask_restful import Api

# Index
from resources.IndexResource import IndexResource

# Visitas
from resources.VisitasResource import VisitasResource, VisitaResource

# Visitantes
from resources.VisitantesResource import VisitantesResource, VisitanteResource

api = Api()

# Index
api.add_resource(IndexResource, '/')

# Visitas
api.add_resource(VisitasResource, '/visitas')
api.add_resource(VisitasResource, '/visita/<int:id>')

# Visitantes
api.add_resource(VisitantesResource, '/visitantes')
api.add_resource(VisitanteResource, '/visitante/<int:id>')

