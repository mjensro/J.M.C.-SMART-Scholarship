#     Program name: J.M.C.-SMART-Scholarship
#     Description: Used as a route to the landing page
#     Author: Michelle Sroka
#Main page when entering website
from flask import Blueprint,render_template

views = Blueprint('views',__name__) #blueprint for flask

@views.route('/')
def home():
    #return "<h1>J.M.C. SMART Scholarship</h1>" #can write html in these defined blocks but its not good practice
    return render_template("home.html")