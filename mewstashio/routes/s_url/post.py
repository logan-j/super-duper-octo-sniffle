from app import app, models, db
from models.url import Url
from flask import request, jsonify, abort
import yaml
import json
import time

@app.route('/', subdomain='url', methods=['POST'])
def post_url():

    data = request.get_json()
    url = Url(**data)
    db.session.add(url)
    db.session.commit()

    return jsonify(urls=[str(url)])
