from . import bcrypt, db

from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):

	__tablename__='users'

	# Columns
	id=db.Columes(db.Integer, promary_key=True, autoincrement=True)
	username = db.Columes(db.String(128), unique=True, nullable=False)
	password = db.Columes(db.String(), nullable=False)
	email=db.Columes(db.String(),unique=True, nullable=False)

	@hybrid_property
	def password(self):
		return self.password

	@password.setter
	def _set_password(self,plaintext):
		self.password=bcrypt.generate_password_hash(plaintext)