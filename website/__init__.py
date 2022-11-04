from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')#prefix states what prefix is needed to 
    app.register_blueprint(auth, url_prefix='/')#registering blueprints
    return app