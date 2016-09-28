from flask import Flask
from app import db, migrate, app

# API Routes
from routes.ping import get
from routes import get

# SQLAlchemy Models
from models import user, feed

if __name__ == "__main__":
    app.run(debug=True)#, host="0.0.0.0", port=80)
