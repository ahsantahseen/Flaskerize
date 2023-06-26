from flask import Flask,request,jsonify
import pymysql
from schema.student import StudentSchema,student_schema,students_schema
from models.student import Student
from db.db import db

#Student API

# 1. Basic CRUD Done
# 2. Needs Authentication using JWT
# 3. Needs Rate Limiting
# 4. Docker Deployment with Nginx


app=Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ahsan:ahsan1234@localhost:3306/student_db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db.init_app(app)


@app.route("/students",methods=['GET'])
def get_students():
    students=Student.query.all()
    result=students_schema.dump(students)
    return jsonify(result)

@app.route("/student/<id>",methods=['GET'])
def get_student(id):
    student=db.session.get(Student,int(id))
    return student_schema.jsonify(student)

@app.route('/student',methods=['POST'])
def add_student():
    name=request.json['name']
    cgpa=request.json['cgpa']
    age=request.json['age']
    semester=request.json['semester']

    new_student=Student(name,cgpa,age,semester)
    db.session.add(new_student)
    db.session.commit()
    return student_schema.jsonify(new_student)

@app.route("/student/<id>",methods=['PUT'])
def update_student(id):
    student=db.session.get(Student,id)

    name=request.json['name']
    cgpa=request.json['cgpa']
    age=request.json['age']
    semester=request.json['semester']

    student.name=name
    student.cgpa=cgpa
    student.age=age
    student.semester=semester
    db.session.commit()
    return student_schema.jsonify(student)

@app.route("/student/<id>",methods=['DELETE'])
def delete_student(id):
    student=db.session.get(Student,id)    
    db.session.delete(student)
    db.session.commit()
    return student_schema.jsonify(student)


if __name__=='__main__':
    app.run(debug=True)
