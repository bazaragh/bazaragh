from flask import Blueprint, render_template
from flask_security import auth_required

bp = Blueprint("bp_chat", __name__)


@bp.route('/messages', methods=["GET"])
@auth_required()
def chat_list():
    return render_template('chat.jinja')


@bp.route('/messages/<int:user_id>', methods=["GET"])
@auth_required()
def user_chat_list():
    return render_template('chat.jinja')
