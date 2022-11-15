#Database schemas
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from os import path

#Registrar Data Store
class Registrar(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique = True) #only 1 email per user
    fName = db.Column(db.String(100))
    lName = db.Column(db.String(100))
    pNum = db.Column(db.String(11))
    zip = db.Column(db.String(5))
    dob = db.Column(db.String(10))
#can prepopulate all data

#applicant data store
class Applicant(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    gender = db.Column(db.String(6))
    academicStatus = db.Column(db.String(9)) #Freshman, Sophomore, Junior, Senior
    cGPA = db.Column(db.Float(5)) #cumulative GPA
    creditHrs = db.Column(db.Integer)
    semGPA=db.Column(db.Float(5)) #semester GPA
    date = db.Column(db.DateTime(timezone=True),default=func.now)#stores current date&time for application being submitted
    user_id = db.Column(db.Integer, db.ForeignKey('registrar.id'))
#can prepopulate some data

#class Accounting
#The committee also requests the tuition amount paid by the student at the beginning of the semester from the “Accounting Data Store” (Student Number and Tuition from latest semester)
#can pre-populate all data

#class Awarded The awarded amount (i.e., tuition amount) will be stored in the “Awarded Data Store
#can prepopulate some data