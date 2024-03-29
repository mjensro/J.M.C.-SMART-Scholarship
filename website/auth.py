#Used to navigate to other pages
import datetime
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import Registrar,Applicant,Accounting,Awarded
from werkzeug.security import generate_password_hash, check_password_hash #might not be needed, currently using to verify email/student id
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint('auth',__name__) #blueprint for flask
"""@auth.route('/create-student', methods = ['GET', 'POST', 'UPDATE']) #Test page for creation of student records, acts as a "sign-up" page
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

    return render_template("sign_up.html", user=current_user)"""


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
                    #return redirect(url_for('views.home'))
                elif user.email!=email:
                    flash('<Email> does not match Registrar Data Store. Updating to new value...', category='warning') 
                    user.email = request.form['email']
                    Registrar(email=email)
                    db.session.commit()
                    flash('Email has been updated', category='success')
                    break
                    #return redirect(url_for('views.home'))
                elif user.id!=id:
                    flash('Data field(s) do not match Registrar Data Store: <ID> – please reenter data', category='error')
                    continue
                else:
                    if user.creditHrs == 0:
                        flash('Cannot apply', category='error')

                    else:  # Will begin to enter data into database
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

                        if applicantCheck:  # Check if applicant is already in the applicant datastore
                            flash('Already applied!', category='error')

                        else:
                            db.session.add(applicant)
                            db.session.commit()
                            flash('Application Submitted', category='success')

                            # Had to send the object this way because the object would be turned into a string.
                            # Redirects to student records page with arguments
                            return redirect(url_for('auth.student', userFname=user.fName, applicantID=applicant.id,
                                                    applicantG=applicant.gender,
                                                    applicantAS=applicant.academicStatus, applicantCGPA=applicant.cGPA,
                                                    applicantCHrs=applicant.creditHrs,
                                                    applicantSGPA=applicant.semGPA, applicantDate=applicant.date))
                    #return redirect(url_for('auth.student'))
                    break
    return render_template("appform.html", user=current_user)

#http://127.0.0.1:5000/student
@auth.route('/student/<applicantID>/<userFname>/<applicantG>/<applicantAS>/<applicantCGPA>/<applicantCHrs>/<applicantSGPA>/<applicantDate>',methods = ['GET','POST'])
def student(applicantID, userFname, applicantG, applicantAS, applicantCGPA, applicantCHrs, applicantSGPA, applicantDate):
    #Description: Function sends arguments to the student.html webpage where jinja code will handle the variables.
    #Pre-condition: applicantID, userFname, applicantG, applicantAS, applicantCGPA, applicantCHrs, applicantSGPA and
    #               applicantDate. Needs to be sent from create_application()
    #Post-condition: parameters to the student.html webpage where jinja code will handle them.
    #Author: Michael Faustino


    return render_template("student.html", userFname=userFname, applicantID=applicantID, applicantG=applicantG,
                           applicantAS=applicantAS, applicantCGPA=applicantCGPA, applicantCHrs=applicantCHrs,
                           applicantSGPA=applicantSGPA, applicantDate=applicantDate)