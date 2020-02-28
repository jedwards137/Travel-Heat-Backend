from flask_restful import Resource
from Model import db, Coordinate, CoordinateSchema, User, UserSchema

user_schema = UserSchema()
coordinates_schema = CoordinateSchema(many=True)

class CoordinatesCollectionResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        user = user_schema.dump(user).data

        coordinates = Coordinate.query.filter_by(user_id=user_id).all()
        coordinates = coordinates_schema.dump(coordinates).data
        response = {'status': 'success', 'user': user, 'coordinates': coordinates}, 200
        return response