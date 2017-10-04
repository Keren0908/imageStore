from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

from .util.validators import Unique
from .models import User


class UsernameEmailPasswordForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(),Email(),Unique(User,User.email,message='There is already an account with the email.')])
	password= PasswordField('Password', validators=[DataRequired()])

