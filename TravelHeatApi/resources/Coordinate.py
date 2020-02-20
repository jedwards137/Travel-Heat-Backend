from flask import Request
from flask_restful import Resource
from Model import db, Coordinate, CoordinateSchema

coordinates_schema = CoordinateSchema(many=True)
coordinate_schema = CoordinateSchema()

class CoordinateResource(Resource):
    def get(self):
        coordinates = Coordinate.query.all()
        coordinates = coordinates_schema.dump(coordinates).data
        response = {'status': 'success', 'data': coordinates}, 200
        return response

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            no_input_response {'message': 'no input provided'}, 400
            return no_input_response
        # validate and deserialize input
        data, errors = coordinate_schema.load(json_data)
        if errors:
            errors_response = errors, 422
            return errors_response
        coordinate = Coordinate(
            latitude = json_data['latitude']
            longitude = json_data['longitude']
            description = json_data['description']
            date_visited = json_data['date_visited']
            user_id = json_data['user_id']
        )

        db.session.add(coodinate)
        db.session.commit()

        result = coordinate_schema.dump(coordinate).data
        success_response = {'status': 'success', 'data': result}, 201
        return success_response