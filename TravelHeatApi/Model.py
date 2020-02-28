from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Coordinate(db.Model):
    __tablename__ = 'coordinates'
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(12,8), nullable=False)
    longitude = db.Column(db.Float(12,8), nullable=False)
    date_visited = db.Column(db.String(16), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('coordinates', lazy='dynamic'))

    def __init__(self, latitude, longitude, user_id, date_visited):
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.date_visited = date_visited


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pin = db.Column(db.String(8), nullable=False)

    def __init__(self, name, email, pin):
        self.name = name
        self.email = email
        self.pin = pin

class UserSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    email = fields.String(required=True)
    pin = fields.String(required=True)

class CoordinateSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    date_visited = fields.DateTime()
