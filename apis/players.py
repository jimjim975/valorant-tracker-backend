from flask import request
from flask_restx import Resource, Namespace
from .Models.player import PlayerModel
from .Schemas.player import PlayerSchema

api = Namespace('games', description='Player matchmaking ranking data')


@api.route('/players')
class PlayersAll(Resource):
    def get(self):
        args = request.args
        username = args.get('username')
        tag = args.get('tag')
        player_data = {'player_data': {}}
        if not args:
            result = PlayerModel.query.all()
            player_data['player_data'] = PlayerSchema().dump(result, many=True)
        elif username and tag:
            result = PlayerModel.query.filter_by(username=username, tag=tag)
            player_data['player_data'] = PlayerSchema().dump(result, many=True)
        else:
            raise Exception

        return player_data
