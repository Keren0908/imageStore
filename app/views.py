
import os
from werkzeug import secure_filename
from wand.image import Image

from flask import render_template, redirect, url_for, request, flash, session,send_from_directory
from flask_login import login_required, login_user, logout_user, current_user

from . import app, db, login_manager
from .models import User,saveImage
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
			login_user(user)
			flash("Sign in successfully.")
			return redirect(url_for('home',username=username))
		else :
			return redirect(url_for('signin_error1'))
		
	return render_template("signin.html")


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('welcome'))

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
				return redirect(url_for('signin'))
		elif db.session.query(User).filter_by(username=username).first() is not None:
			return redirect(url_for("signup_error1"))
	return render_template("signup.html")



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
@login_required
def home(username):
	
	user_id = current_user.get_id()

	# imglist=[]
	# userimg=db.session.query(saveImage).filter_by(username=user_id).all()
	# for item in userimg:
		# imglist.append(item.image_path)

	#show thumbnail:
	imglist=[]
	imgs=db.session.query(saveImage).filter_by(username=user_id).all()
	for img in imgs:
		imglist.append(img.resize_path)


	return render_template('homepage.html',imglist=imglist)
	

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['GET','POST'])
@login_required
def upload():
	if current_user.is_authenticated and request.method == 'POST':
		user_id = current_user.get_id()

	if request.method=='POST':
		file=request.files['file']
		if file and allowed_file(file.filename):
			filename=secure_filename(file.filename)


			path=os.path.join(app.config['UPLOAD_FOLDER'],user_id)

			origin_path=path+'/origin'
			resize_path=path+'/resize'
			rotate_path=path+'/rotate'
			threshold_path=path+'/threshold'
			blur_path=path+'/blur'
			flop_path=path+'/flop'
				
			if not os.path.exists(origin_path):
				os.makedirs(origin_path)
			if not os.path.exists(resize_path):
				os.makedirs(resize_path)
			if not os.path.exists(rotate_path):
				os.makedirs(rotate_path)
			if not os.path.exists(threshold_path):
				os.makedirs(threshold_path)
			if not os.path.exists(blur_path):
				os.makedirs(blur_path)
			if not os.path.exists(flop_path):
				os.makedirs(flop_path)


			
			
			db_origin_path='image/'+user_id+'/origin/'+filename
			db_resize_path='image/'+user_id+'/resize/'+filename
			db_rotate_path='image/'+user_id+'/rotate/'+filename
			db_blur_path='image/'+user_id+'/blur/'+filename
			db_flop_path='image/'+user_id+'/flop/'+filename
			
			filepath=origin_path+'/'+filename
			saveimage=saveImage(user_id,db_origin_path,db_resize_path,db_rotate_path,db_blur_path,db_flop_path)
			
			if db.session.query(saveImage).filter_by(username=user_id,origin_path=db_origin_path).first() is None:
				file.save(filepath)
				db.session.add(saveimage)
				db.session.commit()

				with Image(filename=filepath) as img:
					with img.clone() as i:
						i.resize(int(200),int(i.height * 200/i.width))
						i.save(filename=resize_path+'/'+filename)
					with img.clone() as i:
						i.rotate(90)
						i.save(filename=rotate_path+'/'+filename)
					with img.clone() as i:
						i.flop()
						i.save(filename=flop_path+'/'+filename)
					with img.clone() as i:
						i.gaussian_blur(2,1)
						i.save(filename=blur_path+'/'+filename)



			#thumbnails
			imglist=[]
			imgs=db.session.query(saveImage).filter_by(username=user_id).all()
			for img in imgs:
				imglist.append(img.resize_path)

			return render_template('homepage.html',imglist=imglist)
	return render_template('homepage.html')

@app.route('/test')
@login_required
def test():
	return "just for test"
	

