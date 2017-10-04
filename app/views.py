from flask import render_template, redirect, url_for, request, flash
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

@app.route('/signup',methods=["GET","POST"])
def signup():
	form = SignUpForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, password=form.password.data,email=form.email.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home',username=db.query.first()))
	return render_template('signup.html',form=form)


@app.route('/home/<username>')
def home(username):
	return "Sign in as % s" %username

