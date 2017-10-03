from flask import flask

app = Flask(__name__，instance_relative_config=True)
app.config.from_object('config')
app.config.from_profile('config.py')





