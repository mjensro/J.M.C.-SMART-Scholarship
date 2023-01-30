# J.M.C.-SMART-Scholarship
Created by Team MAM Fall 2022
Michelle Sroka
Michael Faustino

                                                     Operating Environment
Programming Language: Python
Compiler: Visual Studio Code: https://code.visualstudio.com/ (with SQLite extension: SQLite - Visual Studio Marketplace)
Operating system: Windows or Mac
Additional Modules Required: 
Flask: https://flask.palletsprojects.com/en/2.2.x/ ; Used to develop a functioning front end with a python backend
Flask-Login: https://flask-login.readthedocs.io/en/latest/ ; Verify correct usernames and passwords are entered
Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/ ; Combines SQL tables with Python & Flask
Flask-WTF: https://flask-wtf.readthedocs.io/en/1.0.x/ ; Ability to handle form parts of the website to validate login

                                                       File Directory
J.M.C-SMART-SCHOLARSHIP - Main Folder holding all required contents
‘Website’ Folder            -Stores all HTML, Javascript, and backend files
‘Templates’ Folder 	   -Holds all HTML documents within the Website folder
Base.html 	   -Used to build the navigation bar “base” of the website
	Home.html 	   -The default page the server will open on
Appform.html -Used to create application front end
Sign_up.html  -Additional tool for testing purposes, can create 
 student records in the database (Not used in Final Build)
    	Committee_Login_Page.html  -Used for committee members to be authenticated & login
Committee_Dash.html  -Allows Committee members to view and sort all applications
__init__.py -Used to instantiate a database and accept the blueprint 
tables from model.py.
Change Location of lines 12: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/msro/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'
and 35: if not path.exists('sqlite:////Users/msro/Documents/GitHub/J.M.C.-SMART-Scholarship/website/database.db'):
To match the path of wherever your database.db is located on your personal machine, and include ’sqlite:////’ prior to the directory.
Model.py - Outlines the SQL columns associated with all the needed 
      tables for the program
Auth.py  -Used to combine python with website elements, and route data entries so they can be used in comparison statements, etc.
Views.py -Home page Blueprint
Main.py   -Used to launch the program. Once all libraries are installed correctly, it should give you a link to the following: http://127.0.0.1:5000 while running you should be able to insert into any browser and view like a normal website.
Eligibility.py -Handles the eligibility checking and stores them in the applicant database as eligible or non-eligible. non-eligible applicants will be stored with a reason
Committee_Login.py -Handles the login of committee members and their dashboard
  
                                                    Summary Checklist
-Install Python on the preferred operating system
-Install Visual Studio Code 
-Make sure that your VS Code is linked to your preferred python version
-Install SQLite Explorer from the extensions tab if you wish to view the database in a readable matrix form and to test queries
-Install additional modules in your terminal (pip install flask, pip install flask-login, pip install flask-sqlalchemy, pip install flask-wtf) View the website located above if there are difficulties doing these commands.
-Change lines 12 and 35 in the __init__.py file to match the directory of where the database.db file is located on your personal computer. 
-Run __init__.py to instantiate the database with blueprints, it will close itself once it has been completed.
-Run main.py
-Enter this link on a browser while main.py is still running http://127.0.0.1:5000
-Our current database is set with 1000 pre-populated registrar records and 500 applicant records. To test adding a new applicant, you must reference an ID above studentID 0000500, otherwise you will receive an “Already Applied!” Error.
-In order to access the committee page, the login information is as follows: username: CommitteeMemberOne
-password: CommiteeOne123
-Enter some records, then head back into the compiler. Right click on database.db and click “Open Database” to view inserted records. Right click on database.db under the SQLITE EXPLORER and hit “new query” to create a select statement to view any new records that have been created.
