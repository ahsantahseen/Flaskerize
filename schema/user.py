from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

validation_schema_registration = {
    "name": {
        "type": "string",
        "maxlength": 80,
        "required": True
    },
    "email": {
        "type": "string",
        "required": True
    },
    "password": {
        "type": "string",
        "minlength": 5,
        "required": True
    },
}

validation_schema_login = {
    "email": {
        "type": "string",
        "required": True
    },
    "password": {
        "type": "string",
        "minlength": 5,
        "required": True
    },
}


class UserSchema(marshmallow.Schema):
    # The meta data we want to output in our JSON Response
    class Meta:
        fields = ["id", "name", "email", "password"]


user_schema = UserSchema()
users_schema = UserSchema(many=True)
