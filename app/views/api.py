from flask import Blueprint, jsonify
from flask_security import auth_required

from app.app import db
from app.models import Dormitory, Faculty

bp = Blueprint("bp_api", __name__, url_prefix="/api")


@bp.route("/dormitories")
def api_dormitories():
    dorms = db.session.query(Dormitory).all()
    dorms.sort(key=lambda x: int(x.id[2:].replace("DS", "0").strip()))
    results = [{"id": d.id, "text": f"{d.id} {d.name}"} for d in dorms]
    return jsonify({"results": results})


@bp.route("/faculties")
def api_faculties():
    faculties = db.session.query(Faculty).all()
    results = [{"id": f.id, "text": f"W{f.id}"} for f in faculties]
    return jsonify({"results": results})
