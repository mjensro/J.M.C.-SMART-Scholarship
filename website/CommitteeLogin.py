#     Program name: J.M.C.-SMART-Scholarship
#     Description: Committee login handles the login of committee members and their dashboard
#     Author: Michael Faustino
#     Date Created: December 6, 2022

from flask import Blueprint,render_template,flash, redirect, url_for
from flask_login import logout_user, login_required, login_user
from werkzeug.security import check_password_hash
from .models import User, Applicant

cLogin = Blueprint('cLogin',__name__) #blueprint for flask

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class loginForm(FlaskForm): #Form class for entering login info
    userName = StringField("Username", validators=[DataRequired()])
    passWord= PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class applicantIDForm(FlaskForm): #Form class for entering student ID
    id = StringField("Student ID", validators=[DataRequired()])
    submit = SubmitField("Submit")
    displayAll = SubmitField("Display all applicants")



@cLogin.route('/committee-login', methods = ['GET', 'POST'])
def login():
    # Description: Handles the logging in of the committee member
    # Pre-condition: class loginForm
    # Post-condition: redirects them to dashboard page after login
    # Author: Michael Faustino

    form = loginForm()

    if form.validate_on_submit(): #Check for user in user datastore
        user = User.query.filter_by(userName=form.userName.data).first()

        if user: #User exists
            if check_password_hash(user.passwordHash, form.passWord.data): #Checking if password hashes match
                login_user(user) #Creates session for user
                return redirect(url_for('cLogin.dashboard'))
            else:
                flash('Wrong Password!', category='error')

        else: #User does not exist
            flash('Username not found', category='error')

    return render_template("Committee_Login_Page.html", form=form)

@cLogin.route('/committee-dash', methods = ['GET', 'POST'])
@login_required
def dashboard():
    # Description: Handles the committee dashboard.
    #              Specifically handles the entering of a student ID or showing all applicants
    # Pre-condition: class applicantIDForm
    # Post-condition: Sending all the applicants to be shown in Committee_dash.html or
    #                 single applicant in Committee_dash.html
    # Author: Michael Faustino

    form = applicantIDForm()
    applicants = Applicant.query.order_by(Applicant.eligibilityStatus) #Getting all applicants

    if form.validate_on_submit(): #If the submit button is clicked and there is data in the field
        student = Applicant.query.filter_by(id=form.id.data).first() #Get first instance of studentID in applicant datastore
        if student: #If student exists

            #Sends student instead of applicants
            return render_template("Committee_dash.html", form=form, applicants=student)
        else: #No Student existing
            flash('No student found!', category='error')

    #Will execute this if the submit is not clicked
    return render_template("Committee_dash.html", form=form, applicants=applicants)

@cLogin.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    # Description: Logs out the user
    # Pre-condition: user logged in
    # Post-condition: user logged out
    # Author: Michael Faustino

    logout_user()
    flash('Logout Successful', category='success')
    return redirect(url_for('views.home'))