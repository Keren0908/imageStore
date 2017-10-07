import os
from flask import Flask,request,Request,redirect,url_for,render_template,send_from_directory
from werkzeug import secure_filename
from .. import app

UPLOAD_FOLDER= "/Users/akayayy/Pictures/test"
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/homepage',methods=['GET','POST'])
def upload():
	if request.method=='POST':
		file=request.files['file']
		if file and allowed_file(file.filename):
			filename=secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			uploadimage = 
			return redirect(url_for('upload_file',filename=filename))
	return render_template('homepage.html',uploadimage)

@app.route('/homeimg/<filename>')
def upload_file(filename):
	image = send_from_directory(app.config['UPLOAD_FOLDER'],filename)
	return image
