from flask import render_template
from flask_login import login_required, current_user

@app.route('/')
@app.route('/welcome')
def welcome():
	return render_template("welcome2.html")

@app.route('/signin')
def signin():
	return render_template("signin.html")