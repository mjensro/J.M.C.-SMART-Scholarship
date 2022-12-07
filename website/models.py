#Database schemas
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from os import path

#Registrar Data Store
class Registrar(db.Model, UserMixin):
    id = db.Column(db.String(8), primary_key=True)
    fName = db.Column(db.String(100), nullable = False)
    lName = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    pNum = db.Column(db.String(11), nullable = False)
    zip = db.Column(db.String(5), nullable = False)
    dob = db.Column(db.String(10), nullable = False)
    #notes = db.relationship('Applicant')
#can prepopulate all data

#Applicant data store
class Applicant(db.Model):
    id = db.Column(db.String(8),primary_key = True)
    gender = db.Column(db.String(6))
    academicStatus = db.Column(db.String(9)) #Freshman, Sophomore, Junior, Senior
    cGPA = db.Column(db.Float(5)) #cumulative GPA
    creditHrs = db.Column(db.Integer)
    semGPA=db.Column(db.Float(5)) #semester GPA
    date = db.Column(db.DateTime(timezone=True),default=func.now) #default = datetime.utcnow)#stores current date&time for application being submitted
    #user_id = db.Column(db.Integer, db.ForeignKey('Registrar.id'))

    #create string
 #   def __repr__(self):
#        return '<Name %r>' % self.name
#can prepopulate some data


#class Accounting
#The committee also requests the tuition amount paid by the student at the beginning of the semester from the “Accounting Data Store” 
#(Student Number and Tuition from latest semester)
#can pre-populate all data

#class Awarded The awarded amount
# tuition amount
#can prepopulate some data