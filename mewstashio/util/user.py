from flask.ext.stormpath import user

def get_user():
    url = user.get_id()
    return url.split('/')[-1]
