from website import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask import Flask, render_template


#run webpage from this file
#open via http://127.0.0.1:5000

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    