from flask_restful import Resource
from Model import db, User, UserSchema

users_schema = UserSchema(many=True)

class UsersCollectionResource(Resource):
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users).data
        response = {'status': 'success', 'users': users}, 200
        return response