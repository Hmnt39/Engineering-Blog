"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def initialize_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()
        return app