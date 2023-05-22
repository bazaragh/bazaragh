from flask import Blueprint, jsonify

from app.app import db
from app.models import Dormitory, Faculty

bp = Blueprint("bp_api", __name__, url_prefix="/api")


@bp.route("/dormitories")
@bp.route("/dormitories/<string:default>")
def dormitories(default: str = None):
    dorms = db.session.query(Dormitory).all()
    dorms.sort(key=lambda x: int(x.id[2:].replace("DS", "0").strip()))
    results = [{"id": d.id,
                "text": f"{d.id} {d.name}",
                "selected": True if default == d.id else False} for d in dorms]
    return jsonify({"results": results})


@bp.route("/faculties")
@bp.route("/faculties/<string:default>")
def faculties(default: str = None):
    faculties = db.session.query(Faculty).all()
    results = [{"id": f.id,
                "text": f"W{f.id}",
                "selected": True if default == f.id else False} for f in faculties]
    return jsonify({"results": results})
