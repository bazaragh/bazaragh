from datetime import datetime

from flask import Blueprint, jsonify, request, abort
from flask_login import current_user
from flask_security import auth_required

from app.app import db, socketio
from app.models import Dormitory, Faculty, User, Message

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


@bp.route("/message", methods=["POST"])
@auth_required()
def api_message():
    fs_uniquifier = request.get_json()['recipient']
    content = request.get_json()['content']
    recipient = db.session.query(User).filter_by(fs_uniquifier=fs_uniquifier).one_or_none()
    if recipient is None:
        abort(404)
    message = Message(sender=current_user.id,
                      recipient=recipient.id,
                      post_date=datetime.now(),
                      content=content)
    db.session.add(message)
    db.session.commit()
    socketio.emit(fs_uniquifier, {"from": current_user.id, "content": content})
    return jsonify({"result": "success"})


@bp.route("/messages/unread", methods=["GET"])
@auth_required()
def api_unread_messages():
    messages = db.session.query(Message).filter_by(recipient=current_user.id,
                                                   read_date=None).all()
    return jsonify({"unread": len(messages)})


@bp.route('/offer/<int:offer_id>/rating', methods=['POST'])
@auth_required()
def set_user_offer_rating(offer_id):
    rating = request.get_json()['rating']
    print('offer', rating)
    return jsonify({"result": "success"})

@bp.route('/offer/<int:offer_id>/rating', methods=['GET'])
def get_user_offer_rating(offer_id):
    return jsonify({"rating": 3})

@bp.route('/offer/<int:offer_id>/authorRating', methods=['POST'])
@auth_required()
def set_user_author_rating(offer_id):
    rating = request.get_json()['rating']
    print('author', rating)
    return jsonify({"result": "success"})

@bp.route('/offer/<int:offer_id>/authorRating', methods=['GET'])
def get_user_author_rating(offer_id):
    return jsonify({"rating": 4})
