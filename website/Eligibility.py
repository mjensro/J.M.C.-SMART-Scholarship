#Used to navigate to other pages
from flask import Blueprint,redirect,url_for,flash
from .models import Applicant,Registrar
from datetime import date
from . import db
eli = Blueprint('eli',__name__) #blueprint for flask

@eli.route('/eligibilityCheck', methods = ['Get', 'POST'])
def eligibilityCheck():
    applicants = Applicant.query.order_by(Applicant.id)
    today = date.today()
    for applicant in applicants:
        applicantRegist = Registrar.query.filter_by(id=applicant.id).first()
        applicantDob = applicantRegist.dob
        applicantDob = applicantDob.split('/')
        applicantDob = list(map(int, applicantDob))
        age = today.year - applicantDob[2] - ((today.month, today.day) < (applicantDob[0], applicantDob[1]))

        if applicant.cGPA >= 3.2 and applicant.creditHrs >= 12 and age <= 23:
            applicant.eligibilityStatus = "Eligible"

        else:
            applicant.eligibilityStatus = "Non-Eligible"

            if applicant.cGPA < 3.2 and applicant.creditHrs < 12 and age > 23:
                applicant.reason = "Does not meet any requirements."

            else:
                if applicant.cGPA < 3.2:
                    applicant.reason = "Does not meet minimum GPA requirement."

                applicantReason = applicant.reason

                if applicantReason == None:
                    applicantReason = ""

                if applicant.creditHrs < 12:
                    applicant.reason = f"{applicantReason} \n" + "Does not meet minimum credit hours requirement."
                if age > 23:
                    applicant.reason = f"{applicantReason} \n" "Does not meet maximum age requirement."

            db.session.commit()

    flash('Finished checking!', category='success')
    return redirect(url_for('cLogin.dashboard'))

