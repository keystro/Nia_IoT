#!/usr/bin/python3
#!/usr/flask/python3

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from nia.config import Config


db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view='views.login'
login_manager.refresh_view = "views.login"#forces users to re loginin certain cases,eg when user changes password
login_manager.needs_refresh_message = "To protect your account, please reauthenticate to access this page."

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from nia.routes import views
    app.register_blueprint(views)

    return app
