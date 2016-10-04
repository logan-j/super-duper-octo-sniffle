from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from random import randint

class Url(db.Model):
    __tablename__ = 'urls'

    def __init__(self, url, user_id=None):
        self.id = self.generate_url()
        self.url = url
        self.user_id = user_id

    id = db.Column(db.String, primary_key=True)
    url = db.Column(db.String, nullable=False)
    user_id = db.Column(UUID(as_uuid=False), index=True)

    def __repr__(self):
        return "Url(id={id}, url={url})".format(id=self.id, url=self.url)

    def generate_url(self):
        chars = range(48, 58) + range(65, 91) + range(97, 123)
        output = ''
        for _ in xrange(0, 6):
            output += chr(chars[randint(0, len(chars) - 1)])
        return output
