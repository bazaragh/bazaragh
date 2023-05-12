import datetime
import logging
import os
from pathlib import Path

from flask import Flask
from flask_admin import Admin
from flask_babel import Babel
from flask_mailman import Mail
from flask_security import SQLAlchemyUserDatastore, Security, hash_password
from flask_security.models import fsqla
from flask_sqlalchemy import SQLAlchemy

from app.engine.exceptions import exception_handler
from app.forms.security import ExtendedRegisterForm, ExtendedConfirmRegisterForm

admin = Admin(name='BazarAGH.pl - Sprzedawaj po sąsiedzku na BazarAGH.pl', template_mode='bootstrap4')
babel = Babel()
mail = Mail()
db = SQLAlchemy()
security = Security()

OFFERS_IMAGES_DIR = 'offers'
ABSOLUTE_OFFERS_IMAGES_PATH =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', OFFERS_IMAGES_DIR)
Path(ABSOLUTE_OFFERS_IMAGES_PATH).mkdir(exist_ok=True)


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
                                             f"/{app.config['DB_NAME']}?charset=utf8")

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

    babel.init_app(app)
    mail.init_app(app)
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
    from app.utils.mail_util import MailUtil
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.mail_util_cls = MailUtil
    security.init_app(app, user_datastore,
                      register_form=ExtendedRegisterForm,
                      confirm_register_form=ExtendedConfirmRegisterForm)

    # Create roles and admin user
    with app.app_context():
        if not user_datastore.find_role(role="Admin"):
            # noinspection PyArgumentList
            db.session.add(Role(name="Admin"))
        if not user_datastore.find_role(role="Moderator"):
            # noinspection PyArgumentList
            db.session.add(Role(name="Moderator"))
        if not user_datastore.find_role(role="User"):
            # noinspection PyArgumentList
            db.session.add(Role(name="User"))
        if not user_datastore.find_user(email="admin@bazaragh.pl"):
            user_datastore.create_user(
                email="admin@bazaragh.pl",
                password=hash_password("changeme"),
                confirmed_at=datetime.datetime.now(),
                roles=["Admin"]
            )
        db.session.commit()

    admin.init_app(app)

    from app.admin import admin_panel_init
    admin_panel_init(app, admin, db)

    # Register blueprints (views)
    # https://flask.palletsprojects.com/en/2.2.x/blueprints/
    from app.views.main import bp as bp_main
    app.register_blueprint(bp_main)

    from app.views.api import bp as bp_api
    app.register_blueprint(bp_api)

    from app.views.user import bp as bp_user
    app.register_blueprint(bp_user)

    from app.views.settings import bp as bp_settings
    app.register_blueprint(bp_settings)

    from app.views.offer import bp as bp_offer
    app.register_blueprint(bp_offer)

    # Import and register blueprints here

    return app
