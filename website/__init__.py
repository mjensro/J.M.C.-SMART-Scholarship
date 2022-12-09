from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path
# from . import models

db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/StimmyStation/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'
    #'sqlite:////C:/flasker/J.M.C.-SMART-Scholarship/website/database.db' for Michelles windows setup
    #'sqlite:////Users/msro/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'
    #'sqlite:////website/database.db'
    #'f'sqlite:////{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
   # db=SQLAlchemy()
    db.init_app(app)

    #Login manager for Committee Page
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'cLogin.login'

    from.models import User
    @login_manager.user_loader
    def load_user(userName):
        return User.query.get(str(userName))
    #END LOGIN MANAGER STUFF


    from .views import views
    from .auth import auth
    from .CommitteeLogin import cLogin
    from .Eligibility import eli

    app.register_blueprint(views, url_prefix='/')#prefix states what prefix is needed to 
    app.register_blueprint(auth, url_prefix='/')#registering blueprints
    app.register_blueprint(cLogin, url_prefix='/')
    app.register_blueprint(eli, url_prefix='/')# registering blueprints
    
    #from .models import Registrar, Applicant #import other databases
    from . import models
    create_database(app)
    #with app.app_context():
     #   db.create_all()
    return app

def create_database(app):#if database DNE, it creates it, otherwise leave it alone as to not overwrite already existing data
    if not path.exists('sqlite:////Users/StimmyStation/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'): #+ DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created New Database!')
            print('Exiting Program')
    else: 
        print("Database Already Exists")
        print("Exiting Program")