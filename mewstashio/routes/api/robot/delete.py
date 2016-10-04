from app import app, models
from models.robot import Robot
from flask import request
import json

@app.route('/api/robot', methods=['POST'])
def post_robot():
    data = json.loads(request.get_data())
    robot = Robot(**data)
