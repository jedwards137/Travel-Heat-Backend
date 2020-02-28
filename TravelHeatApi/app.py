from flask import Blueprint
from flask_restful import Api
from resources.UserResource import UserResource
from resources.UsersCollectionResource import UsersCollectionResource
from resources.CoordinateResource import CoordinateResource
from resources.CoordinatesCollectionResource import CoordinatesCollectionResource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

#Routes
api.add_resource(UserResource, '/user', '/user/<int:user_id>')
api.add_resource(UsersCollectionResource, '/users')

api.add_resource(CoordinateResource, '/coordinate', '/coordinates')
api.add_resource(CoordinatesCollectionResource, '/user/<int:user_id>/coordinates')