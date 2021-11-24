#Main_Project_Blog init
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)

##############
###DB Setup###
##############

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

################
###Blueprints###
################

from main_project_blog.core.views import core
from main_project_blog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)