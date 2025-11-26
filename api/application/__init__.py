# api/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application import config

# Globals
db = SQLAlchemy()


def init_app():
    """Initialise application"""
    app = Flask(__name__)
    app.config.from_object(config.Config)

    from application import routes
    from application import models

    app.register_blueprint(routes.api_bp)

    db.init_app(app)

    with app.app_context():
        models.init_db()

    return app


app = init_app()
