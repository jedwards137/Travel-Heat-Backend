from flask import request
from flask_restful import Resource
from Model import db, User, Coordinate, CoordinateSchema

coordinates_schema = CoordinateSchema(many=True)
coordinate_schema = CoordinateSchema()

class CoordinateResource(Resource):
    def get(self):
        coordinates = Coordinate.query.all()
        coordinates = coordinates_schema.dump(coordinates).data
        response = {'status': 'success', 'coordinates': coordinates}, 200
        return response

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            response = {'status': 'failed', 'errors': 'no body received'}, 400
            return response

        data, errors = coordinate_schema.load(json_data)
        
        if errors:
            response = {'status': 'failed', 'errors': errors}, 422
            return response

        coordinate = Coordinate(
            latitude = json_data['latitude'],
            longitude = json_data['longitude'],
            date_visited = json_data['date_visited'],
            user_id = json_data['user_id']
        )

        db.session.add(coordinate)
        db.session.commit()

        result = coordinate_schema.dump(coordinate).data
        success_response = {'status': 'success', 'coordinate': result}, 201
        return success_response