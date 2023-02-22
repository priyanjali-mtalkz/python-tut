from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validate

level = ["EASY","MEDIUM","HARD"]
class user_schema(Schema):
    userId = fields.Integer(
        required = True,
        validate = validate.Length(min=0,max=10)
    )
    Score = fields.Integer(
        required = True
    )

    Time = fields.Integer(
        required = True
    )
    Level = fields.Str(
        required = True,
        validate = validate.Oneof(level)
    )




