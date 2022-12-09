from flask import Blueprint,render_template,request,flash, redirect, url_for
from flask_login import logout_user, login_required, login_user
from werkzeug.security import check_password_hash
cLogin = Blueprint('cLogin',__name__) #blueprint for flask
from .models import User

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
    userName = StringField("Username", validators=[DataRequired()])
    passWord= PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

@cLogin.route('/committee-login', methods = ['GET', 'POST'])
def login():
    form = loginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(userName=form.userName.data).first()

        if user:
            if check_password_hash(user.passwordHash, form.passWord.data):
                login_user(user)
                flash('Hello!', category='success')
                return redirect(url_for('cLogin.dashboard'))
            else:
                flash('Wrong Password!', category='error')

        else:
            flash('Username not found', category='error')

    return render_template("Committee_Login_Page.html", form=form)

@cLogin.route('/committee-dash', methods = ['GET', 'POST'])
@login_required
def dashboard():
    return render_template("Committee_dash.html")