import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from logger import logger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
api = Api(app)
db = SQLAlchemy(app)

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    components = relationship('CarComponent', back_populates='car')

class CarComponent(db.Model):
    __tablename__ = 'car_components'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    car_id = db.Column(db.Integer, ForeignKey('cars.id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    car = relationship('Car', back_populates='components')

class CarComponentCreator(Resource):
    def get(self):
        logger.info('Hey there')
        return {'Hello': 'World'}

api.add_resource(CarComponentCreator, '/')

if __name__ == '__main__':
    db.create_all()
    app.run(port=os.getenv('PORT', 5001))