from flask import Blueprint, render_template

bp = Blueprint("bp_main", __name__)


# Here you can read about routing:
# https://flask.palletsprojects.com/en/2.0.x/api/#url-route-registrations
# https://hackersandslackers.com/flask-routes/
@bp.route('/')
def main_get():
    return render_template('main.html.jinja', message="Hello, world!")
