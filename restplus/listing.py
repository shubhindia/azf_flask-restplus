from flask import Flask, abort, request, jsonify
from flask_restful import Resource, Api
import json
import logging


app = Flask(__name__)
api = Api(app)

class Keepalive(Resource):
    def get(self):
        logging.error("Hiiiiiii")
        return "OK"

class Test(Resource):
    def get(self):
        data = {"app":"flask restplus"}
        return jsonify(data)


api.add_resource(Keepalive, '/keepalive')
api.add_resource(Test, '/test')