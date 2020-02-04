import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from logger import logger

# Flask/SQLAlchemy setup and config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:////tmp/test.db')
api = Api(app)
db = SQLAlchemy(app)

# ORM - Cars and Car components
class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    components = relationship('CarComponent', back_populates='car')

class CarComponent(db.Model):
    __tablename__ = 'car_components'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    car_id = db.Column(db.Integer, ForeignKey('cars.id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    car = relationship('Car', back_populates='components')

parser = reqparse.RequestParser()
parser.add_argument('name')

# Our internal car creation API
class CarComponentCreator(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        logger.info(f'c2: Received request to extrapolate car components for {args["name"]}')
        car = Car(name=args['name'])
        engine = CarComponent(name='engine', car=car)
        wheels = CarComponent(name='wheels', car=car)
        body = CarComponent(name='body', car=car)
        db.session.add(car)
        db.session.add(engine)
        db.session.add(wheels)
        db.session.add(body)
        db.session.commit()
        db.session.refresh(car)
        logger.info(f'c2: Car created {car.name} -- id: {car.id} with components')
        return {'created': True, 'car.id': car.id}

api.add_resource(CarComponentCreator, '/')

if __name__ == '__main__':
    db.create_all()
    # NOTE: you MUST bind to 0.0.0.0 inside the container
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5001))