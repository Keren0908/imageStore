
import os
from werkzeug import secure_filename
from wand.image import Image

from flask import render_template, redirect, url_for, request, flash, session,send_from_directory
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
		user = User.query.filter_by(username=username).first()
		
		if user.is_correct_password(password):
			login_user(u)
			flash("Sign in successfully.")
			return redirect(url_for('home',username=username))
		else :
			return redirect(url_for('signin_error1'))
		
	return render_template("signin.html")



@app.route('/signup',methods=["GET","POST"])
def signup():
	#form = SignUpForm(request.form)
	#if form.validate_on_submit():
	if request.method=='POST':
		username=request.form.get('username')
		password=request.form.get('password')
		email=request.form.get('email')
		user = User(username,password,email)

		if db.session.query(User).filter_by(username=username).first() is None:
			if db.session.query(User).filter_by(email=email).first() is not None:
				return redirect(url_for("signup_error2"))
			elif db.session.query(User).filter_by(email=email).first() is None:
				db.session.add(user)
				db.session.commit()
				flash("Sign up successfully.")
				return redirect(url_for('home',username=username))
		elif db.session.query(User).filter_by(username=username).first() is not None:
			return redirect(url_for("signup_error1"))
	return render_template("signup.html")


@app.route('/signin/error',methods=['GET','POST'])
def signin_error1():
	return "Please check your log in information!"


@app.route('/signup/error1',methods=['GET','POST'])
def signup_error1():
	return "This username has been registered."

@app.route('/signup/error2',methods=['GET','POST'])
def signup_error2():
	return "This email has been used."

#---------------picture upload--------------

ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

@app.route('/<username>/home',methods=['GET','POST'])
def home(username):
	return "Home  %s" %username

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/homepage',methods=['GET','POST'])
def upload():
	if request.method=='POST':
		file=request.files['file']
		if file and allowed_file(file.filename):
			filename=secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return redirect(url_for('upload_file',filename=filename))
	return render_template( 'homepage.html')

@app.route('/homeimg/<filename>',methods=['GET','POST'])
def upload_file(filename):
	img=url_for('static',filename=filename)
	return render_template('homepage.html',img=img)
	

