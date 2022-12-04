from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
# from . import models

db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/msro/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'
    #'sqlite://///C:/flasker/J.M.C.-SMART-Scholarship/website/database.db' for windows setup
    #'sqlite:///////Users/msro/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'
    #'sqlite:///////website/database.db'
    #'f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
   # db=SQLAlchemy()
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')#prefix states what prefix is needed to 
    app.register_blueprint(auth, url_prefix='/')#registering blueprints
    
    #from .models import Registrar, Applicant #import other databases
    from . import models
    create_database(app)
    #with app.app_context():
     #   db.create_all()
    return app

def create_database(app):#if database DNE, it creates it, otherwise leave it alone as to not overwrite already existing data
    if not path.exists('sqlite:////Users/msro/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'): #+ DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')
