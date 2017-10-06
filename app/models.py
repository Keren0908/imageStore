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