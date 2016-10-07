from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask.ext.stormpath import StormpathManager
from util import config

config = config.make(filepath='.env')

# initialize
app = Flask(__name__)

# configs
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DATABASE', 'URI')
app.config['SECRET_KEY'] = 'thisisaprivatestring'
app.config['STORMPATH_API_KEY_FILE'] = config.get('STORMPATH', 'API_KEY_PATH')
app.config['STORMPATH_API_KEY_ID'] = config.get('STORMPATH', 'API_ID')
app.config['STORMPATH_API_KEY_SECRET'] = config.get('STORMPATH', 'SECRET_KEY')
app.config['STORMPATH_APPLICATION'] = config.get('STORMPATH', 'APPLICATION')

# register extensions
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
stormpath_manager = StormpathManager(app)

# SQLAlchemy models
import models
from models import robot, url
