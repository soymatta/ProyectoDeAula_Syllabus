import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.secret_key = os.urandom(50)
app.template_folder = '../templates'
app.static_folder = '../static'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/syllabus"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)