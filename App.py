from os import environ
from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from marshmallow import Schema, fields
from sqlalchemy import create_engine, Table, Column, String, MetaData
from flask_cors import CORS
from sqlalchemy.dialects.postgresql import Insert as ins


app = Flask(__name__)
CORS(app)
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
                  Column('mmr', String),
                  Column('rank', String),
                  Column('date', String),
                  Column('tag', String))


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
    rank = fields.Str()
    date = fields.Str()
    tag = fields.Str()


class MMRSchema(Schema):
    mmr_data = fields.Nested(DataSchema)


@api.route('/mmr')
class MMR(Resource):
    def post(self):
        data = MMRSchema().load(request.json)['mmr_data']
        table = meta.tables['mmrproddata']
        stmt = ins(table).values(username=data['username'],
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
                                         mmr=data['mmr'],
                                         rank=data['rank'],
                                         date=data['date'],
                                         tag=data['tag']).on_conflict_do_nothing(index_elements=['username', 'date'])

        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

        return {'result': 'success'}
    def get(self):
        args = request.args
        user = args['username']
        tag = args['tag']
        with engine.connect() as conn:
            table = mmr_table.select().where(mmr_table.columns.username == user).where(mmr_table.columns.tag == tag)

            result = conn.execute(table).fetchall()
            total = []
            for thing in result:
                total.append(list(thing))
                print(thing)
            
            return { "result": list(total) }
            
