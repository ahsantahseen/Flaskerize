from flask import Flask, request, jsonify, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from dotenv import load_dotenv

import os
import pymysql
import uuid
import jwt
import datetime

from schema.student import student_schema, students_schema, validation_schema_students
from schema.user import user_schema, users_schema
from models.student import Student
from models.user import User
from db.db import db
from utils import validate_json


# Student API

# 1. CRUD
# 2. Authentication using JWT
# 3. Rate Limiting

app = Flask(__name__)
load_dotenv()
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=['35 per hour'],
    storage_uri='memory://'
)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQL_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET')

db.init_app(app)


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorator


with app.app_context():
    db.create_all()


@app.route("/students", methods=['GET'])
@token_required
def get_students(current_user):
    students = Student.query.all()
    result = students_schema.dump(students)
    return jsonify(result)


@app.route("/student/<id>", methods=['GET'])
@token_required
def get_student(current_user, id):
    student = db.session.get(Student, int(id))
    return student_schema.jsonify(student)


@app.route('/student', methods=['POST'])
@token_required
def add_student(current_user):
    if validate_json(validation_schema_students, request.json):
        name = request.json['name']
        cgpa = request.json['cgpa']
        age = request.json['age']
        semester = request.json['semester']

        new_student = Student(name, cgpa, age, semester)
        db.session.add(new_student)
        db.session.commit()
        return student_schema.jsonify(new_student)
    else:
        return make_response(jsonify({"Error": 'Incomplete/Incorrect Data, Please Try Again!'}), 400)


@app.route("/student/<id>", methods=['PUT'])
@token_required
def update_student(current_user, id):
    student = db.session.get(Student, id)
    if student:
        if validate_json(validation_schema_students, request.json):
            name = request.json['name']
            cgpa = request.json['cgpa']
            age = request.json['age']
            semester = request.json['semester']

            student.name = name
            student.cgpa = cgpa
            student.age = age
            student.semester = semester
            db.session.commit()
            return student_schema.jsonify(student)
        else:
            return make_response(jsonify({"Error": 'Incomplete/Incorrect Data, Please Try Again!'}), 400)
    else:
        return make_response(jsonify({"Error": 'Student Not Found'}), 404)


@app.route("/student/<id>", methods=['DELETE'])
@token_required
def delete_student(current_user, id):
    student = db.session.get(Student, id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return student_schema.jsonify(student)
    else:
        return make_response(jsonify({"Error": 'Student Not Found'}), 404)


@app.route("/register", methods=['POST'])
def register_user():
    name = request.json['name']
    email = request.json['email']
    password = generate_password_hash(
        request.json['password'], method='scrypt')
    new_user = User(name, email, password)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@app.route("/login", methods=['POST'])
def login_user():
    user = User.query.filter_by(email=request.json['email']).first()
    if check_password_hash(user.password, request.json['password']):
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=45)}, app.config['SECRET_KEY'], "HS256")
        return jsonify({"token": token})
    return make_response(jsonify({"Error": 'Login Required'}), 401)


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG_MODE'), host='0.0.0.0')
