from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Required, Email

from .util.validators import Unique
from .models import User


class SignUpForm(Form):
	username = StringField('Username', validators=[Required()])
	password= PasswordField('Password', validators=[Required()])
	email = StringField('Email',validators=[Required(),Email(),Unique(User,User.email,message='There is already an account with the email.')])

