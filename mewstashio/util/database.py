from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session(engine_path):
    e = create_engine(engine_path)
    Session = sessionmaker(bind=e)
    return Session()
