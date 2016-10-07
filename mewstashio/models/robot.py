from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Robot(db.Model):
    __tablename__ = 'robots'

    id = db.Column(
        UUID(as_uuid=False),
        primary_key=True,
    )
    user_id = db.Column(db.String, nullable=False, index=True)

    name = db.Column(db.String)

    def __init__(self, user_id, name=None, id=str(uuid.uuid4())):
        self.user_id = user_id
        self.name = name
        self.id = id

    def __repr__(self):
        return "Robot(id={id})".format(id=self.id)
