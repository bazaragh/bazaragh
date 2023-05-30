from datetime import datetime

from flask import Blueprint, render_template, abort
from flask_login import current_user
from flask_security import auth_required

from app.app import db
from app.models import User, Message
from app.utils.chat import generate_threads, fetch_messages

bp = Blueprint("bp_chat", __name__, url_prefix='/messages')


@bp.route('/', methods=["GET"])
@auth_required()
def chat_list():
    threads = generate_threads()

    return render_template('chat.jinja',
                           threads=threads,
                           messages=None)


@bp.route('/<int:user_id>', methods=["GET"])
@auth_required()
def user_chat_list(user_id: int):
    threads = generate_threads()
    messages = sorted(fetch_messages(user_id), key=lambda msg: msg['post_date'])
    unread = db.session.query(Message).filter_by(sender=user_id,
                                                 recipient=current_user.id,
                                                 read_date=None).all()
    for m in unread:
        m.read_date = datetime.now()
    db.session.commit()
    recipient = db.session.query(User).filter_by(id=user_id).one_or_none()
    if recipient is None:
        abort(404)
    recipent_name = f"{recipient.first_name} {recipient.last_name}"
    return render_template('chat.jinja',
                           recipient_id=user_id,
                           recipient=recipient.fs_uniquifier,
                           recipent_name=recipent_name,
                           threads=threads,
                           messages=messages)
