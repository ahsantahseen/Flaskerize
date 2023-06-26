from flask_marshmallow import Marshmallow

marshmallow=Marshmallow()

class StudentSchema(marshmallow.Schema):
    #The meta data we want to output in our JSON Response
    class Meta:
        fields=["id","name","semester","cgpa","age"]

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

