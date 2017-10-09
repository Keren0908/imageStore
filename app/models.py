from flask_login import UserMixin
from . import bcrypt, db
from sqlalchemy.ext.hybrid import hybrid_property



class User(db.Model,UserMixin):

	__tablename__='users'

	# Columns
	id=db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(64), nullable=False)
	password = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(128),unique=True, nullable=False)

	def __init__(self, username, password,email):
		self.username = username
		self.password = self._set_password(password)
		self.email = email
	

	
	def _set_password(self,plaintext):
		return bcrypt.generate_password_hash(plaintext)

	def is_correct_password(self, plaintext):
		return bcrypt.check_password_hash(self.password, plaintext)

	def __repr__(self):
		return self.username

		

class saveImage(db.Model,UserMixin):

	__tablename__='user_image'

	id=db.Column(db.Integer, primary_key=True, autoincrement=True)
	username=db.Column(db.String(64),nullable=False)
	origin_path=db.Column(db.String(1024),unique=True,nullable=False)
	resize_path=db.Column(db.String(1024),unique=True,nullable=False)
	rotate_path=db.Column(db.String(1024),unique=True,nullable=False)
	blur_path=db.Column(db.String(1024),unique=True,nullable=False)
	flop_path=db.Column(db.String(1024),unique=True,nullable=False)




	def __init__(self,username,origin_path,resize_path,rotate_path,blur_path,flop_path):
		self.username=username
		self.origin_path=origin_path
		self.resize_path=resize_path
		self.rotate_path=rotate_path
		self.blur_path=blur_path
		self.flop_path=flop_path
		

