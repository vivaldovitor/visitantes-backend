from flask_restful import Api

# Index
from resources.IndexResource import IndexResource

# Visitantes
from resources.VisitantesResource import VisitantesResource, VisitanteResource

api = Api()

# Index
api.add_resource(IndexResource, '/')

# Visitantes
api.add_resource(VisitantesResource, '/visitantes')
api.add_resource(VisitanteResource, '/visitante/<int:id>')

