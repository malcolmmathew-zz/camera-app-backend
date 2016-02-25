from flask_restful import Resource
from flask import request

users = {}

class GetUsers(Resource):
	def get(self):
		return {"users": users}

class AddUser(Resource):
	def put(self, user_id):
		users[user_id] = request.form['data']
		return {user_id: users[user_id]}
