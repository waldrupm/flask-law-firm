from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)  # TODO Edit config class for Postgres when ready.

    db.init_app(app)
    migrate.init_app(app)

    # login_manager.init_app(app)
    # TODO configure login_view and login_message_category when users setup.

    # with app.app_context():
    #     from app import routes

    from app.blueprints.main.routes import main
    app.register_blueprint(main)

    return app


from app import models
