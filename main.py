#     Program name: J.M.C.-SMART-Scholarship
#     Description: "Main" File to Run the Flask App
#     Author: Michelle Sroka

from website import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask import Flask, render_template


#Run webpage from this file
#open via http://127.0.0.1:5000
#Michelle is running on: Python 3.10.8 & Flask-SQLAlchemy 3.0.2 & Flask-Login 0.6.2

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
