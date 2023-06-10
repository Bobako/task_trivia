import configparser
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


config = configparser.ConfigParser()
config.read("config.ini")

if os.environ.get("USE_ENV"):
    config = {key:dict(section) for key, section in dict(config).items()}
    config["DATABASE"]["uri"] = os.environ.get("DATABASE_URI")
    config["SITE"]["port"] = os.environ.get("SITE_PORT")

app = Flask(__name__)
app.secret_key = config["SITE"]["secret_key"]
app.config['SQLALCHEMY_DATABASE_URI'] = config["DATABASE"]["uri"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from app import models, routes

with app.app_context():
    db.create_all()