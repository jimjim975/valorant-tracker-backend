from flask_restx import Api
from .players import api as player_api

api = Api(
    title='Valorant MMR API',
    doc='/doc',
    version='1.0',
    description='Valorant matchmaking data'
)

api.add_namespace(player_api)
