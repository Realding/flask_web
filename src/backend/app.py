from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .config import configs

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    CORS(app)
    db.init_app(app)
    return app
