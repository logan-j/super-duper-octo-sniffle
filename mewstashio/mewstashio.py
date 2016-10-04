from flask import Flask
from app import db, migrate, app

# API Routes
from routes.ping import get
from routes import get
from routes.api.robot import get, post
from routes.s_url import get, post, delete

# SQLAlchemy Models

if __name__ == "__main__":
    app.config['SERVER_NAME'] = 'localhost.io:5000'
    app.run(debug=True, host="0.0.0.0", port=5000)
