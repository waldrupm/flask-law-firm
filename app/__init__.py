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
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'account.login'
    login_manager.login_message_category = 'warning'

    with app.app_context():
        from app import errors

    from app.blueprints.main.routes import main
    app.register_blueprint(main)

    from app.blueprints.account.routes import account
    app.register_blueprint(account)

    return app


from app import models
