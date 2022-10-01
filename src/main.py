from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


def create_app():
    # Create the flask app object
    app = Flask(__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)

    return app
