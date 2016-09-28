from app import app

import routes.get

# Add all route imports here
# ...

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
