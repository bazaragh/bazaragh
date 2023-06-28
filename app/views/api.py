from datetime import datetime

from flask import Blueprint, jsonify, request, abort, make_response
from flask_login import current_user
from flask_security import auth_required

from app.app import db, socketio
from app.models import Dormitory, Faculty, Offer, OfferScore, User, Message, UserScore

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


@bp.route('/offer/<int:offer_id>/rating', methods=['POST'])
@auth_required()
def set_user_offer_rating(offer_id):
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    
    is_new = False
    offer_score = db.session.query(OfferScore).filter_by(
        offer=offer_id, 
        seller=offer.author, 
        customer=current_user.id).one_or_none()
    if offer_score is None:
        is_new = True
        offer_score = OfferScore(
            offer=offer_id, 
            seller=offer.author, 
            customer=current_user.id)
        
    offer_score.score = request.get_json()['rating']
    if is_new:
        db.session.add(offer_score)
    db.session.commit()
    return {"result": "success"}

@bp.route('/offer/<int:offer_id>/rating', methods=['GET'])
def get_user_offer_rating(offer_id):
    rating = 0
    if not current_user.is_authenticated:
        return {"rating": 0}
    
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    offer_score = db.session.query(OfferScore).filter_by(
        offer=offer_id, 
        customer=current_user.id).one_or_none()
    if offer_score is not None:
        rating = offer_score.score
        
    return {"rating": rating}

@bp.route('/offer/<int:author_id>/author-rating', methods=['POST'])
@auth_required()
def set_user_author_rating(author_id):
    is_new = False
    author = db.session.query(User).filter_by(id=author_id).one_or_none()
    if author is None:
        abort(404)
    user_score = db.session.query(UserScore).filter_by(
        seller=author_id, 
        customer=current_user.id).one_or_none()
    if user_score is None:
        is_new = True
        user_score = UserScore(
            seller=author_id, 
            customer=current_user.id)
        
    user_score.score = request.get_json()['rating']
    if is_new:
        db.session.add(user_score)
    db.session.commit()
    return {"result": "success"}

@bp.route('/offer/<int:author_id>/author-rating', methods=['GET'])
def get_user_author_rating(author_id):
    rating = 0
    if not current_user.is_authenticated:
        return {"rating": 0}
    author = db.session.query(User).filter_by(id=author_id).one_or_none()
    if author is None:
        abort(404)
    user_score = db.session.query(UserScore).filter_by(
        seller=author_id, 
        customer=current_user.id).one_or_none()
    if user_score is not None:
        rating = user_score.score
        
    return {"rating": rating}
