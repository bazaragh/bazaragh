import os
from flask import Flask, jsonify
from werkzeug.debug import DebuggedApplication


# Flask quickstart:
# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# Flask factory pattern:
# https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # Load config from file config.py
    app.config.from_pyfile("config.py")

    # Ensure the instance folder exists - nothing interesting
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Setup custom "Not found" page
    # https://flask.palletsprojects.com/en/2.0.x/errorhandling/#custom-error-pages
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({
            "message": "not found",
            "code": "404"
        }), 404

    # Register blueprints (views)
    # https://flask.palletsprojects.com/en/2.0.x/blueprints/
    from app.api.index import bp as bp_index
    app.register_blueprint(bp_index)

    return app
