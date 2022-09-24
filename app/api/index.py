from flask import Blueprint, jsonify, request

bp = Blueprint("bp_index", __name__)


# Here you can read about routing:
# https://flask.palletsprojects.com/en/2.0.x/api/#url-route-registrations
# https://hackersandslackers.com/flask-routes/
@bp.route('/')
def index_get():
    return jsonify("Hello world")


@bp.route('/hello/<name>', methods=["GET"])
def name_get(name):
    return jsonify(f"Hello {name}")


@bp.route('/hello', methods=["POST"])
def name_post():
    name = request.get_data(as_text=True)
    return jsonify(f"Hello {name}")
