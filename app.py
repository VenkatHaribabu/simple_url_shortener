from flask import Flask
from routes import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )