from app import app, models, db
from models.robot import Robot
from flask import request
import json

@app.route('/api/robot', methods=['POST'])
def post_robot():
    try:
        data = json.loads(request.get_data())
        robot = Robot(**data)
    except:
        return "Your model sucks"

    db.session.add(robot)
    db.session.commit()
    return robot.id
