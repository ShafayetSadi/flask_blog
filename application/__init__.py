from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = '0270e77bd9e8c8ab55ab4b2cbcccdaeb'
#app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from application import routes