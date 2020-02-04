import os
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from logger import logger

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', help='Make and model of car')

# Our client (external) API
class CreateCar(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        logger.info(f'c1: Received request to create car: {args["name"]}')
        resp = requests.post('http://c2:5001/', data={'name': args['name']})
        return resp.json(), resp.status_code


api.add_resource(CreateCar, '/')

if __name__ == '__main__':
    # NOTE: you MUST bind to 0.0.0.0 inside the container
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))