from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

from .resources.user import GetUsers, AddUser

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

api = Api(app)
api.add_resource(GetUsers, '/users/')
api.add_resource(AddUser, '/users/<string:user_id>')
