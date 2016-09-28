from flask import Flask

from util import config


config = config.make(filepath='.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DATABASE', 'URI')
