from os import environ
from flask import Flask, request
from flask_restx import Resource, Api
from marshmallow import Schema, fields
from sqlalchemy import create_engine, Table, Column, String, MetaData

app = Flask(__name__)
api = Api(app)
engine = create_engine(environ['DB_URL'])
meta = MetaData()
meta.create_all(engine)

mmr_table = Table('mmrproddata', meta,
                  Column('username', String),
                  Column('kills', String),
                  Column('assists', String),
                  Column('deaths', String),
                  Column('kd', String),
                  Column('charactername', String),
                  Column('roundsplayed', String),
                  Column('timeplayed', String),
                  Column('mapname', String),
                  Column('rankimage', String),
                  Column('mmrdiff', String),
                  Column('score', String),
                  Column('mmr', String))


class DataSchema(Schema):
    username = fields.Str()
    kills = fields.Str()
    assists = fields.Str()
    deaths = fields.Str()
    kd = fields.Str()
    character_name = fields.Str()
    rounds_played = fields.Str()
    time_played = fields.Str()
    map_name = fields.Str()
    ranked_image = fields.Str()
    mmr_diff = fields.Str()
    score = fields.Str()
    mmr = fields.Str()


class MMRSchema(Schema):
    mmr_data = fields.Nested(DataSchema)


@api.route('/mmr')
class MMR(Resource):
    def post(self):
        data = MMRSchema().load(request.json)['mmr_data']
        stmt = mmr_table.insert().values(username=data['username'],
                                         kills=data['kills'],
                                         assists=data['assists'],
                                         deaths=data['deaths'],
                                         kd=data['kd'],
                                         charactername=data['character_name'],
                                         roundsplayed=data['rounds_played'],
                                         timeplayed=data['time_played'],
                                         mapname=data['map_name'],
                                         rankimage=data['ranked_image'],
                                         mmrdiff=data['mmr_diff'],
                                         score=data['score'],
                                         mmr=data['mmr'])

        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

        return {'message': 'success'}
