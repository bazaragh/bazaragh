import os
from flask import Flask, render_template


# Flask quickstart:
# https://flask.palletsprojects.com/en/2.2.x/quickstart/
# Flask factory pattern:
# https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/
def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # Load config from file config.py
    app.config.from_pyfile("config.py")

    if os.path.exists("config.local.py"):
        app.config.from_pyfile("../config.local.py")

    # Ensure the instance folder exists - nothing interesting
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Setup custom "Not found" page
    # https://flask.palletsprojects.com/en/2.2.x/errorhandling/#custom-error-pages
    @app.errorhandler(404)
    def page_not_found(e: Exception):
        return render_template('error.html.jinja', code=404, message=e), 404

    # Register blueprints (views)
    # https://flask.palletsprojects.com/en/2.2.x/blueprints/
    from app.views.main import bp as bp_main
    app.register_blueprint(bp_main)

    return app
