from flask_restful import Api, Resource, reqparse, abort
from flask import Flask, jsonify

from firebase_connect import get_rfb, update_first, update_second, update_third
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class ConnectYOT(Resource):

    def get(self):
        return jsonify(get_rfb())
    
class UpdateYOT(Resource):
    def put(self, word):
        parser.add_argument('message')

        args = parser.parse_args()
        
        if word == "word1":
            update_first(args["message"])
        elif word == "word2":
            update_second(args["message"])
        elif word == "word3":
            update_third(args["message"])
        else:
            abort(404)

api.add_resource(ConnectYOT, "/api")
api.add_resource(UpdateYOT, "/api/<string:word>")