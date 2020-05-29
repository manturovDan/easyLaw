from flask import Flask
from src.auth.auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print(app.url_map)
    app.run()
