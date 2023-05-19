from flask_login import current_user
from sqlalchemy import text

from app.app import db
from app.models import User


def fetch_user(user_id: int):
    user = db.session.query(User).filter_by(id=user_id).one_or_none()
    if user is None:
        return "konto usunięte"
    return f"{user.first_name} {user.last_name}"


def fetch_preview(user_id: int):
    result = db.session.execute(text("""
        SELECT content, post_date
        FROM message
        WHERE sender = :u OR recipient = :u
        ORDER BY post_date DESC
        LIMIT 1
    """), {'u': user_id})
    result = [row for row in result]
    preview = [row[0] for row in result]
    post_date = [row[1] for row in result]
    if len(preview) < 1:
        return "brak wiadmości", 0
    return preview[0][:32], post_date[0]


def generate_threads():
    # Find senders
    senders = db.session.execute(text("""
            SELECT DISTINCT(sender)
            FROM message
            WHERE recipient = :u
        """), {'u': current_user.id})
    senders = [row[0] for row in senders]

    # Find recipients
    recipients = db.session.execute(text("""
            SELECT DISTINCT(recipient)
            FROM message
            WHERE sender = :u
        """), {'u': current_user.id})
    recipients = [row[0] for row in recipients]

    threads = []

    for user_id in [*{*senders, *recipients}]:
        user = fetch_user(user_id)
        preview, post_date = fetch_preview(user_id)
        threads.append({"user": user,
                        "user_id": user_id,
                        "preview": preview,
                        "post_date": post_date})

    return sorted(threads, key=lambda t: t['post_date'], reverse=True)


def fetch_messages(user_id: int):
    result = db.session.execute(text("""
        SELECT sender, post_date, content
        FROM message
        WHERE (sender = :u AND recipient = :c) OR (sender = :c AND recipient = :u)
    """), {'u': user_id, 'c': current_user.id})
    result = [row for row in result]

    return [{'author': row[0],
             'post_date': row[1],
             'content': row[2]} for row in result]
