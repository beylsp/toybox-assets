from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db  = SQLAlchemy()


def create_app(config_name):
    app = Flask(
        __name__,
        static_folder="../static",
        template_folder="../templates"
    )
    app.config.from_object(config[config_name])

    db.init_app(app)

    from webapp.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app