from . import bcrypt, db

from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):

	__tablename__='users'

	# Columns
	id=db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(128), unique=True, nullable=False)
	password = db.Column(db.String(), nullable=False)
	email=db.Column(db.String(),unique=True, nullable=False)

	@hybrid_property
	def password(self):
		return self.password

	@password.setter
	def _set_password(self,plaintext):
		self.password=bcrypt.generate_password_hash(plaintext)

	def is_correct_password(self, plaintext):
		return bcrypt.check_password_hash(self.password, plaintext)