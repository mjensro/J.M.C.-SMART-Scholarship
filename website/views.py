from flask import Blueprint

views = Blueprint('views',__name__) #blueprint for flask

@views.route('/')
def home():
    return "<h1>J.M.C. SMART Scholarship</h1>"