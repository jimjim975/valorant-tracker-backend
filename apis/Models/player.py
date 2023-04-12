from sqlalchemy import UniqueConstraint, Column, Integer, String
from app import db


class PlayerModel(db.Model):
    __tablename__ = 'mmrdata'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    kills = Column(String)
    assists = Column(String)
    deaths = Column(String)
    kd = Column(String)
    charactername = Column(String)
    roundsplayed = Column(String)
    timeplayed = Column(String)
    mapname = Column(String)
    rankimage = Column(String)
    mmrdiff = Column(String)
    score = Column(String)
    mmr = Column(String)
    rank = Column(String)
    date = Column(String)
    tag = Column(String)
    UniqueConstraint('username', 'date', name='constraint')
