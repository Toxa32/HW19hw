from marshmallow import Schema, fields

from setup_db import user_db


class User(user_db.Model):
    __tablename__ = 'user'
    id = user_db.Column(user_db.Integer, primary_key=True)
    username = user_db.Column(user_db.String)
    password = user_db.Column(user_db.String)
    role = user_db.Column(user_db.String)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
