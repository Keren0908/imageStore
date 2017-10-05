from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_required, login_user, logout_user, current_user

from . import app, db
from .models import User
from .forms import SignUpForm

@app.route('/')
@app.route('/welcome')
def welcome():
	return render_template("welcome2.html")

@app.route('/signin',methods=["GET","POST"])
def signin():
	return render_template("signin.html")

@app.route('/signup',methods=["GET"])
def signup():
	return render_template("signup.html")

@app.route('/signup',methods=['POST'])
def signup_submit():
	username=request.form.get('username')
	password=request.form.get('password')
	email=request.form.get('email')
	user = User(username,password,email)

	db.session.add(user)
	db.session.commit()
	return redirect(url_for('home',username=username))
	


@app.route('/home/<username>',methods=['GET','POST'])
def home(username):
	return "dfdd %s" %username

