from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Coordinate import CoordinateResource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

#Routes
api.add_resource(Hello, '/Hello')
api.add_resource(CoordinateResource, '/Coordinate')