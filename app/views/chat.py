from flask import Blueprint, render_template
from flask_security import auth_required

from app.app import db
from app.models import Message
from app.utils.chat import generate_threads, fetch_messages

bp = Blueprint("bp_chat", __name__)


@bp.route('/messages', methods=["GET"])
@auth_required()
def chat_list():
    threads = generate_threads()

    return render_template('chat.jinja',
                           threads=threads,
                           messages=None)


@bp.route('/messages/<int:user_id>', methods=["GET"])
@auth_required()
def user_chat_list(user_id: int):
    threads = generate_threads()
    messages = sorted(fetch_messages(user_id), key=lambda m: m['post_date'])
    return render_template('chat.jinja',
                           threads=threads,
                           messages=messages)
