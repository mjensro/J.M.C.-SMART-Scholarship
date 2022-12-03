#Used to navigate to other pages
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import Registrar,Applicant
from werkzeug.security import generate_password_hash, check_password_hash #might not be needed, currently using to verify email/student id
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint('auth',__name__) #blueprint for flask
#submit = post request
@auth.route('/create-student', methods = ['GET', 'POST', 'UPDATE'])
def create_student():
    if request.method == 'POST':
        id = request.form.get('ID')
        fName = request.form.get('fName')
        lName = request.form.get('lName')
        email = request.form.get('email')
        pNum = request.form.get('pNum')
        zip = request.form.get('zip')
        dob = request.form.get('dob')

        user = Registrar.query.filter_by(email=email).first()
        if user:
            flash('Email already exists',category='error')
        elif user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        else:
            new_user = Registrar(email=email, fName=fName,lName=lName,pNum=pNum,zip=zip,dob=dob,id=id)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home')) #change routing page

    return render_template("sign_up.html", user=current_user)


@auth.route('/create-application', methods = ['GET', 'POST', 'UPDATE'])
def create_application():
    if request.method == 'POST':
        id = request.form.get('ID')
        fName = request.form.get('fName')
        lName = request.form.get('lName')
        email = request.form.get('email')
        pNum = request.form.get('pNum')
        zip = request.form.get('zip')
        dob = request.form.get('dob')

        user = Registrar.query.filter_by(id=id).first()
        if user:
            if check_password_hash(user.id,id):
                 flash('Log in Successful', category='success')
            else:
                flash('Incorrect Submission, Try Again',category='error')
        else:
            flash('Email does not exist',category='error')
    #code is currently set up to create application inputs as "new users", its not looking for pre-existing IDs yet
        new_applicant = Registrar(email=email,fName=fName,lName=lName,pNum=pNum,zip=zip,dob=dob,id=id)
        db.session.add(new_applicant)# add a new user,etc.
        db.session.commit() #commit changes to db, update file
        flash('Application Submitted', category='success')
        return redirect(url_for('auth.student'))#'views.home' = forward to next page with student GPA,etc. from Applicant Database



       #if no Student Number match:
       #  flash('No Student Number Match – please reenter data', category = 'error')
       #elif Student Number matches but one or more of the fields: First Name, Last Name, Zip Code, and Date of Birth do not match “Registrar Data Store” report back an
            #flash('Data field(s) do not match Registrar Data Store: <list the one or more mismatched data field names> – please reenter data', category ='error')
       #elif Student Number, First Name, Last Name, Zip Code, Date of Birth do match “Registrar Data Store” but Phone Number and/or Email Address do not match – report back a message 
        #"<non-matching data field(s)> do not match Registrar Data Store. Update to new value(s) (y/n)?”
        #If “y” …. Update fields are report message “Fields updated” Continue with next step.
        #If “n” …. Report message “Please reenter the data”. Repeat edits.
        #else:
            #add student to database
            #flash('Application Accepted',category='success')
            #pass
    #data = request.form
    #print(data)
    return render_template("appform.html")

#http://127.0.0.1:5000/student/Michelle
@auth.route('/student',methods = ['GET', 'POST', 'UPDATE'])
def student():#new_applicant):
#    if request.method == 'POST':
     #   new_applicant = request.form.get('fName')
    return render_template("student.html")#, name=new_applicant.fName) #passing name from def
    #return "<h1>Welcome {}!</h1>".format(name)


    #db.session.add() add a new user,etc.
    #db.session.commit() commit changes to db, update file
