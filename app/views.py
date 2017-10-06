from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_required, login_user, logout_user, current_user

from . import app, db, login_manager
from .models import User
from .forms import SignUpForm

@app.route('/')
@app.route('/welcome')
def welcome():
	return render_template("welcome2.html")

@app.route('/signin',methods=["GET","POST"])
def signin():
	if request.method == 'POST':
		username=request.form.get('username')
		password=request.form.get('password')
		user = User.query.filter_by(username=username).all()
		if user is not None:
			for u in user:
				if u.is_correct_password(password):
					login_user(u)
					flash("Sign in successfully.")
					return redirect(url_for('home',username=username))
	return render_template("signin.html")



@app.route('/signup',methods=["GET","POST"])
def signup():
	form = SignUpForm(request.form)
	if form.validate_on_submit():
		username=form.username.data
		password=form.password.data
		email=form.email.data
		user = User(username,password,email)
		db.session.add(user)
		db.session.commit()
		flash("Sign up successfully.")
		return redirect(url_for('home',username=username))
	
	return render_template("signup.html",form=form)


@app.route('/signup/error',methods=['GET','POST'])
def signup_error():
	return "There exists an account with this email."


@app.route('/home/<username>',methods=['GET','POST'])
def home(username):
	return "Home  %s" %username

