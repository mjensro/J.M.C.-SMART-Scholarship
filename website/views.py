#Main page when entering website
from flask import Blueprint,render_template

views = Blueprint('views',__name__) #blueprint for flask

@views.route('/')
def home():
    #return "<h1>J.M.C. SMART Scholarship</h1>"
    return render_template("home.html")