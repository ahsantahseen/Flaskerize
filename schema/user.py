from flask_marshmallow import Marshmallow

marshmallow=Marshmallow()

class UserSchema(marshmallow.Schema):
    #The meta data we want to output in our JSON Response
    class Meta:
        fields=["id","name","email","password"]

user_schema = UserSchema()
users_schema = UserSchema(many=True)

