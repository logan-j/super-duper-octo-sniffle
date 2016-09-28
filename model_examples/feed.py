from database import db
from app import app
from flask_migrate import Migrate
migrate = Migrate(app, db)
class Feed(db.Model):
    __tablename__ = 'feeds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
