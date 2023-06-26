from db.db import db

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    age=db.Column(db.Integer)
    cgpa=db.Column(db.Float)
    semester=db.Column(db.Integer)

    def __init__(self, name,cgpa,age,semester):
      self.name = name
      self.cgpa = cgpa
      self.age = age
      self.semester = semester  