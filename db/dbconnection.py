from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
from flask_restful import Resource, Api, reqparse
from sqlalchemy import Table, Column, Integer, String, MetaData
import requests
import json
import csv
import pandas as pd
import os
import urllib
from smb.SMBHandler import SMBHandler
opener = urllib.request.build_opener(SMBHandler)
import shutil
import urllib.request as req
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time

db_string = "postgresql://mmrtracker:CgUKz3!j63bY@db.mmrtracker.com:5432/mmrdata"
db = create_engine(db_string)

meta = MetaData(db)
mmr_table = Table('mmrdata', meta,
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


now = datetime.now()
dt_string = str(now.strftime("%m/%d/%Y %H:%M:%S"))



decoded_lines = data.decode("utf-8")
data = decoded_lines.split()

csv_reader = csv.reader(data, delimiter=",")
