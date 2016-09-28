from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from util import config

# config = config.make(filepath='.env')
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DATABASE', 'URI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost:5432/postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
