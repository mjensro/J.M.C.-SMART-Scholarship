#Used to navigate to other pages
import datetime
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import Registrar,Applicant,Accounting,Awarded
from werkzeug.security import generate_password_hash, check_password_hash #might not be needed, currently using to verify email/student id
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint('auth',__name__) #blueprint for flask
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

        user = Registrar.query.filter_by(email=email,id=id).first() #makes sure there is no previous entries w/ this same email & id
        #email=request.form.get("email")

        if user: #if it already exists, else say if not user for something that should exist
            flash('ID already exists',category='error')
 #       elif user.email == email:
 #           flash('Email already exists',category='error')
        else:
            new_user = Registrar(email=email, fName=fName,lName=lName,pNum=pNum,zip=zip,dob=dob,id=id)
            db.session.add(new_user)
            db.session.commit()
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
            while user.id == id:
                if user.fName!=fName:
                    flash('Data field(s) do not match Registrar Data Store: <First Name> – please reenter data',category='error')
                    break
                elif user.lName!=lName:
                    flash('Data field(s) do not match Registrar Data Store: <Last Name> – please reenter data',category='error')
                    break                        
                elif user.zip!=zip:
                    flash('Data field(s) do not match Registrar Data Store: <Zip Code> – please reenter data',category='error')   
                    break      
                elif user.dob!=dob:
                    flash('Data field(s) do not match Registrar Data Store: <Date of Birth> – please reenter data',category='error')
                    break
                elif user.pNum!=pNum:
                    flash('<Phone Number> does not match Registrar Data Store. Updating to new value...', category='warning')
                    user.pNum = request.form['pNum']
                    Registrar(pNum=pNum)
                    db.session.commit()
                    flash('Phone Number has been updated', category='success')
                    break
                    #return redirect(url_for('auth.student'))
                elif user.email!=email:
                    flash('<Email> does not match Registrar Data Store. Updating to new value...', category='warning') 
                    user.email = request.form['email']
                    Registrar(email=email)
                    db.session.commit()
                    flash('Email has been updated', category='success')
                    break
                    #return redirect(url_for('auth.student'))
                elif user.id!=id:
                    flash('Data field(s) do not match Registrar Data Store: <ID> – please reenter data', category='error')
                    continue
                else:
                    #return redirect(url_for('auth.student'))
                    break

            if user.creditHrs == 0:
                flash('Cannot apply', category='error')

            else:
                applicant = Applicant(id=user.id,
                                      gender=user.gender,
                                      academicStatus=user.academicStatus,
                                      cGPA=user.cGPA,
                                      creditHrs=user.creditHrs,
                                      semGPA=user.semGPA,
                                      date=datetime.datetime.now(),
                                      eligibilityStatus=None,
                                      reason=None)
                applicantCheck = applicant.query.filter_by(id=applicant.id).first()

                if applicantCheck:
                    flash('Already applied!', category='error')

                else:
                    db.session.add(applicant)
                    db.session.commit()
                    flash('Application Submitted', category='success')

                    print(applicant.gender, user.fName)

                    return redirect(url_for('auth.student',userFname=user.fName, applicantID=applicant.id, applicantG=applicant.gender,
                               applicantAS=applicant.academicStatus, applicantCGPA=applicant.cGPA, applicantCHrs=applicant.creditHrs,
                                applicantSGPA=applicant.semGPA, applicantDate=applicant.date))

    return render_template("appform.html", user=current_user)


    # new_applicant = Registrar(email=email,fName=fName,lName=lName,pNum=pNum,zip=zip,dob=dob,id=id)
    # db.session.add(new_applicant)# add a new user,etc.
    #  db.session.commit() #commit changes to db, update file

    #   return redirect(url_for('auth.student'))#'views.home' = forward to next page with student GPA,etc. from Applicant Database

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

#http://127.0.0.1:5000/student
@auth.route('/student/<applicantID>/<userFname>/<applicantG>/<applicantAS>/<applicantCGPA>/<applicantCHrs>/<applicantSGPA>/<applicantDate>',methods = ['GET','POST'])
def student(applicantID, userFname, applicantG, applicantAS, applicantCGPA, applicantCHrs, applicantSGPA, applicantDate):#new_applicant):
    return render_template("student.html", userFname=userFname, applicantID=applicantID, applicantG=applicantG,
                           applicantAS=applicantAS, applicantCGPA=applicantCGPA, applicantCHrs=applicantCHrs,
                           applicantSGPA=applicantSGPA, applicantDate=applicantDate)#, name=new_applicant.fName) #passing name from def
    #return "<h1>Welcome {}!</h1>".format(name)


    #db.session.add() add a new user,etc.
    #db.session.commit() commit changes to db, update file
