#Used to navigate to other pages
from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__) #blueprint for flask
#submit = post request
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
@auth.route('/student/<name>',methods = ['GET', 'POST', 'UPDATE'])
def student(name):
    return render_template("student.html", user_name=name) #passing name from def
    #return "<h1>Welcome {}!</h1>".format(name)