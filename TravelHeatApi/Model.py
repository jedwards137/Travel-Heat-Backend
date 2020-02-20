from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Coordinate(db.Model):
    __tablename__ = 'coordinates'
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Decimal(12,8), nullable=False)
    longitude = db.Column(db.Decimal(12,8), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    date_visited = db.Column(db.TIMESTAMP, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('coordinates', lazy='dynamic' ))

    def __init__(self, latitude, longitude, description, date_visited, user_id);
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.date_visited = date_visited
        self.user_id = user_id


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


class UserSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)


class CoordinateSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    latitude = fields.Integer(required=True)
    longitude = fields.Integer(required=True)
    date_visited = fields.DateTime()
    user_id = fields.Integer(required=True)