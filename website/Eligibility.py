#     Program name: J.M.C.-SMART-Scholarship
#     Description: Eligibility.py handles the eligibility checking and stores them into the applicant database as
#                  eligible or non-eligible. non-eligible applicants will be store with a reason
#     Author: Michael Faustino
#     Date Created: December 7, 2022

from flask import Blueprint,redirect,url_for,flash
from .models import Applicant,Registrar
from datetime import date
from . import db
eli = Blueprint('eli',__name__) #blueprint for flask

@eli.route('/eligibilityCheck', methods = ['Get', 'POST'])
def eligibilityCheck():
    # Description: Checks applicant's eligibility based on cumulative gpa, applicant credit hours, and their age
    # Pre-condition: applicants in applicant datastore
    # Post-condition: applicant's Eligibility Status updated to eligible or non-eligible.
    #                 Non-eligible will have their reasons updated too. Will reflect on table in Committe_dash.html
    # Author: Michael Faustino

    applicants = Applicant.query.order_by(Applicant.id) #Retrieve all applicants
    today = date.today()
    
    if applicants is not iter: #Check if only one applicant in applicant datastore
        applicantRegist = Registrar.query.filter_by(id=applicants[0].id).first()  # Used to get dob from registrar
        applicantDob = applicantRegist.dob
        applicantDob = applicantDob.split('/')  # splits the dob into a list where the / is present
        applicantDob = list(map(int, applicantDob))  # turns the list from str to int
        age = today.year - applicantDob[2] - ((today.month, today.day) < (
        applicantDob[0], applicantDob[1]))  # gets the applicant's age based on today

        applicants[0].reason = ""
        
        if applicants[0].cGPA >= 3.2 and applicants[0].creditHrs >= 12 and age <= 23: #Eligibility rules fulfilled
            applicants[0].eligibilityStatus = "Eligible"

        else: #Eligibility rules not fulfilled
            applicants[0].eligibilityStatus = "Non-Eligible"

            if applicants[0].cGPA < 3.2 and applicants[0].creditHrs < 12 and age > 23: #All eligibility rules failed
                applicants[0].reason = "Does not meet any requirements."

            else: #Checks for individual rules that failed
                if applicants[0].cGPA < 3.2:
                    applicants[0].reason = "Does not meet minimum GPA requirement."

                applicantReason = applicants[0].reason #Used to concatenate any additional rules broken to the reason attribute

                if applicantReason == None: # Used to check if passes cumulative GPA rule to clear None out of reason
                    applicantReason = ""

                if applicants[0].creditHrs < 12:
                    applicants[0].reason = f"{applicantReason} \n" + "Does not meet minimum credit hours requirement."
                    applicantReason = applicants[0].reason
                if age > 23:
                    applicants[0].reason = f"{applicantReason} \n" + "Does not meet maximum age requirement."

    else:
        for applicant in applicants:
            applicantRegist = Registrar.query.filter_by(id=applicant.id).first() #Used to get dob from registrar
            applicantDob = applicantRegist.dob
            applicantDob = applicantDob.split('/') #splits the dob into a list where the / is present
            applicantDob = list(map(int, applicantDob)) #turns the list from str to int
            age = today.year - applicantDob[2] - ((today.month, today.day) < (applicantDob[0], applicantDob[1])) #gets the applicant's age based on today

            applicant.reason = ""

            if applicant.cGPA >= 3.2 and applicant.creditHrs >= 12 and age <= 23: #Eligibility rules fulfilled
                applicant.eligibilityStatus = "Eligible"

            else: #Eligibility rules not fulfilled
                applicant.eligibilityStatus = "Non-Eligible"

                if applicant.cGPA < 3.2 and applicant.creditHrs < 12 and age > 23: #All eligibility rules failed
                    applicant.reason = "Does not meet any requirements."

                else: #Checks for individual rules that failed
                    if applicant.cGPA < 3.2:
                        applicant.reason = "Does not meet minimum GPA requirement."

                    applicantReason = applicant.reason #Used to concatenate any additional rules broken to the reason attribute

                    if applicantReason == None: # Used to check if passes cumulative GPA rule to clear None out of reason
                        applicantReason = ""

                    if applicant.creditHrs < 12:
                        applicant.reason = f"{applicantReason} \n" + "Does not meet minimum credit hours requirement."
                        applicantReason = applicant.reason
                    if age > 23:
                        applicant.reason = f"{applicantReason} \n" + "Does not meet maximum age requirement."

    db.session.commit()

    flash('Finished checking!', category='success')
    return redirect(url_for('cLogin.dashboard'))

