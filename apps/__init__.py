"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Universal DB object
db = SQLAlchemy()
migrate = Migrate()


def initialize_app():
    """
    Construct the core application.
    Initialize DB object with configurations.
    Import routes in App Context only
    """

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from . import routes

        return app
