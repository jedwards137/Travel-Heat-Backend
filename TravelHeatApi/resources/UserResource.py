from flask import request
from flask_restful import Resource
from Model import db, User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        user = user_schema.dump(user).data
        response = {'status': 'success', 'user': user}, 200
        return response

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            response = {'status': 'failed', 'errors': 'no body received'}, 400
            return response
        
        data, errors = user_schema.load(json_data)
        
        if errors:
            response = {'status': 'failed', 'errors': errors}, 422
            return response

        users_exist = len(data) > 0
        if users_exist:
            user = User.query.filter_by(name=data['name']).first()
            if user:
                response = {'status': 'failed', 'errors': 'user already exists'}, 400
                return response

        user = User(
            name=json_data['name'], 
            email=json_data['email'], 
            pin=json_data['pin']
        )
        
        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user).data
        response = {'status': 'success', 'user': user}, 201
        return response

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            response = {'status': 'failed', 'errors': 'no body received'}, 400
            return response
        
        data, errors = user_schema.load(json_data)

        if errors:
            response = {'status': 'failed', 'errors': errors}, 422
            return response
        
        no_users_stored = len(data) == 0
        if no_users_stored:
            response = {'status': 'failed', 'errors': 'no users'}, 400
            return response

        user = User.query.filter_by(id=data['id']).first()

        if not user:
            response = {'status': 'failed', 'errors': 'user does not exist'}, 400
            return response
        
        user.name = data['name']
        user.email = data['email']
        
        db.session.commit()
        
        result = user_schema.dump(user).data
        response = {'status': 'success', 'user': user}, 204
        return response