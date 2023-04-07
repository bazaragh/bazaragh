import datetime
import logging
import os
from pathlib import Path

from flask import Flask, render_template
from flask_security import SQLAlchemyUserDatastore, Security, hash_password
from flask_security.models import fsqla
from flask_sqlalchemy import SQLAlchemy

from app.engine.exceptions import exception_handler

db = SQLAlchemy()


# Flask quickstart:
# https://flask.palletsprojects.com/en/2.2.x/quickstart/
# Flask factory pattern:
# https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/
def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # Load config from file config.py
    app.config.from_pyfile("config.py")
    app.config.from_pyfile("../config.local.py")

    app.config["SQLALCHEMY_DATABASE_URI"] = (f"mariadb://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}"
                                             f"@{app.config['DB_HOST']}:{app.config['DB_PORT']}"
                                             f"/{app.config['DB_NAME']}")
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # Collect nice logs for debugging
    Path(f"{app.root_path}/{app.config['DEBUG_LOG']}").touch(exist_ok=True)
    Path(f"{app.root_path}/{app.config['ERROR_LOG']}").touch(exist_ok=True)

    logging.basicConfig(
        filename=f"{app.root_path}/{app.config['DEBUG_LOG']}",
        level=logging.DEBUG,
        format=f'[%(asctime)s][%(levelname)s][%(name)s][%(threadName)s] %(message)s'
    )

    # Ensure the instance folder exists - nothing interesting
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_error_handler(Exception, exception_handler)

    @app.errorhandler(404)
    @app.errorhandler(405)
    def _handle_api_error(ex):
        return exception_handler(ex)

    db.init_app(app)

    with app.app_context():
        db.reflect()

    # Configure roles
    from sqlalchemy import Column, Integer, ForeignKey
    fsqla.FsModels.db = db
    fsqla.FsModels.user_table_name = "user"
    fsqla.FsModels.role_table_name = "role"
    fsqla.FsModels.roles_users = db.Table(
        "roles_users",
        Column("user_id", Integer(), ForeignKey(f"user.id")),
        Column("role_id", Integer(), ForeignKey(f"role.id")),
        extend_existing=True
    )

    # Setup Flask-Security
    from app.models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)

    # Create roles and admin user
    with app.app_context():
        if not user_datastore.find_role(role="Admin"):
            db.session.add(Role(name="Admin"))
        if not user_datastore.find_role(role="Moderator"):
            db.session.add(Role(name="Moderator"))
        if not user_datastore.find_role(role="User"):
            db.session.add(Role(name="User"))
        if not user_datastore.find_user(email="test@sokoloowski.pl"):
            user_datastore.create_user(
                email="test@sokoloowski.pl",
                password=hash_password("test"),
                confirmed_at=datetime.datetime.now(),
                roles=["Admin"]
            )
        db.session.commit()

    # Register blueprints (views)
    # https://flask.palletsprojects.com/en/2.2.x/blueprints/
    from app.views.main import bp as bp_main
    app.register_blueprint(bp_main)

    # Import and register blueprints here

    return app
