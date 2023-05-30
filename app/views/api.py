from datetime import datetime

from flask import Blueprint, jsonify, request, abort, make_response
from flask_login import current_user
from flask_security import auth_required

from app.app import db, socketio
from app.models import Dormitory, Faculty, User, Message

bp = Blueprint("bp_api", __name__, url_prefix="/api")


@bp.route("/dormitories")
@bp.route("/dormitories/<string:default>")
def api_dormitories(default: str = None):
    dorms = db.session.query(Dormitory).all()
    dorms.sort(key=lambda x: int(x.id[2:].replace("DS", "0").replace("ne", "-1").strip()))
    results = [{"id": d.id,
                "text": f"{d.id} {d.name}" if not d.id == 'None' else d.name,
                "selected": True if default == d.id else False} for d in dorms]
    return {"results": results}


@bp.route("/faculties")
@bp.route("/faculties/<string:default>")
def api_faculties(default: str = None):
    faculties = db.session.query(Faculty).all()
    results = [{"id": f.id,
                "text": f"W{f.id}" if not f.id == 'None' else f.name,
                "selected": True if default == f.id else False} for f in faculties]
    return {"results": results}


@bp.route("/message", methods=["POST"])
@auth_required()
def api_message():
    fs_uniquifier = request.get_json()['recipient']
    content = request.get_json()['content'].strip()
    recipient = db.session.query(User).filter_by(fs_uniquifier=fs_uniquifier).one_or_none()
    if recipient is None:
        abort(404)

    if len(content) == 0:
        abort(make_response(jsonify(result="error",
                                    description="Cannot send empty message"), 400))

    message = Message(sender=current_user.id,
                      recipient=recipient.id,
                      post_date=datetime.now(),
                      content=content)
    db.session.add(message)
    db.session.commit()
    socketio.emit(fs_uniquifier, {"from": current_user.id, "content": content})
    return {"result": "success"}


@bp.route("/messages/unread", methods=["GET"])
@auth_required()
def api_unread_messages():
    messages = db.session.query(Message).filter_by(recipient=current_user.id,
                                                   read_date=None).all()
    return {"unread": len(messages)}
