from . import db

class User(db.Model):

	__tablename__='users'

	# Columns
	id=db.Columes(db.Integer, promary_key=True, autoincrement=True)
	username = db.Columes(db.String(128), unique=True, nullable=False)
	password = db.Columes(db.String(), unique=True, nullable=False)
	email=db.Columes(db.String(),unique=True, nullable=False)