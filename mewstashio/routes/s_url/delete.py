from app import app, models, db
from models.url import Url
from flask import abort

@app.route('/<string:url_id>', methods=['DELETE'], subdomain='url')
def delete_url(url_id):
    try:
        url = Url.query.get(url_id)
        if url == None:
            abort(404)
        db.session.delete(url)
        db.session.commit()
    except:
        abort(400)

    return jsonify(**url)
