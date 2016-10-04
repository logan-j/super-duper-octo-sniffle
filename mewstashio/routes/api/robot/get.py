from app import app, models
from models.robot import Robot
from flask import request


@app.route('/api/robot/<uuid:robot_id>', methods=['GET'])
def get_robot(robot_id):
    r = Robot.query.get(robot_id)
    return str(r)

@app.route('/api/robot', methods=['GET'])
def get_robot_by_filter():
    return str(request.args)
