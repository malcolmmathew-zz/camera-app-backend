from flask_restful import Resource

class PostImage(Resource):
	def get(self):
		user_names = ['krandhaw, m5mathew, z5haque, yoloswaggins']
		return {'names': user_names}

class GetImage(Resource):
	def get(self):
		return 