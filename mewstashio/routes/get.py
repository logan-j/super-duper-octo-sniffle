from app import app

@app.route('/', methods=['GET'])
def index():
    return "I Love Shawn <3"
