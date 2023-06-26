from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

validation_schema_students = {
    "name": {
        "type": "string",
        "maxlength": 80,
        "required": True
    },
    "age": {
        "type": "integer",
        "min": 18,
        "required": True
    },
    "cgpa": {
        "type": "float",
        "required": True
    },
    "semester": {
        "type": "integer",
        "min": 1,
        "required": True
    },
}


class StudentSchema(marshmallow.Schema):
    # The meta data we want to output in our JSON Response
    class Meta:
        fields = ["id", "name", "semester", "cgpa", "age"]


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
