#!/usr/bin/python3
#!/usr/flask/python3

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from nia.config import Config


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from nia.routes import views
    app.register_blueprint(views)

    return app