from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__, instance_relative_config = True)

app.config.from_object('config')
app.config.from_pyfile('config.py')



app.config['UPLOAD_FOLDER']='app/static/image'

db = SQLAlchemy(app)

bcrypt=Bcrypt(app)


from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "signin"

@login_manager.user_loader
def load_user(userid):
	return User.query.filter(User.id==userid).first()



from app import views


