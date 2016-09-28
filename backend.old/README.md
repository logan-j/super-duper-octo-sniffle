backend
=======

RESTful JSON API built with Python 2.7 and Flask.


# Running
```
cd /path/to/backend/project/backend
python backend/backend.py
```

# Create A Route
Example

1. ```mkdir backend/routes/ping```
2. ```touch backend/routes/ping/get.py```
3. Add the following to **backend/routes/ping/get.py**...
```
    from app import app

    @app.route('/ping', methods=['GET'])
    def ping():
        return "Ping!"
```
4. Your **backend/backend.py** file should look something like this...
```
    from app import app

    import routes.get

    from routes.ping import get # This is the magic line you should add

    if __name__ == "__main__":
        app.run(debug=True)
```


## Config
The config file is located in the 'backend/.env'. An example of a '.env' is below. You'll need to create this yourself.

```
[DATABASE]
URI = sqlite:////dev.db'
```
