from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return {"message": "hellow world"}

    def post(self):
        return {"message": "posted!"}