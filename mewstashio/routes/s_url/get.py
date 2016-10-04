from app import app, models
from models.url import Url
from flask import abort, redirect, jsonify, request, render_template

@app.route('/<string:url_id>', subdomain='url', methods=['GET'])
def get_url(url_id):
    url = Url.query.get(url_id)
    if url == None:
        abort(404)
    return redirect(url.url)

@app.route('/', subdomain='url', methods=['GET'])
def get_url_page():
    urls = Url.query.filter_by(user_id=request.cookies.get('mewstashio')).all()
    # return jsonify(urls=[str(url) for url in urls])
    return render_template('url.html')
