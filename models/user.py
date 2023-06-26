from db.db import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    email=db.Column(db.String(80))
    password=db.Column(db.String(300))

    def __init__(self,name,email,password):
      self.name = name
      self.email = email
      self.password = password
