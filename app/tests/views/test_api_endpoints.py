import json

from app.app import db


def test_dormitories(client):
    with client:
        response = client.get("/api/dormitories")
        assert response.is_json
        assert "results" in response.json.keys()
        for r in response.json["results"]:
            assert "id" in r
            assert "text" in r


def test_faculties(client):
    with client:
        response = client.get("/api/faculties")
        assert response.is_json
        assert "results" in response.json.keys()
        for r in response.json["results"]:
            assert "id" in r
            assert "text" in r


def test_api_message(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_socketio_emit = mocker.patch("app.views.api.socketio.emit")
        recipient = 'c6a04d0809b7498fb7b8bcb6369e2218'
        content = 'test'
        data = {'recipient': recipient,
                'content': content}
        response = client.post(
            "/api/message", data=json.dumps(data), content_type='application/json')

        assert response.is_json
        assert "result" in response.json.keys()
        assert response.json["result"] == 'success'

        from app.models import Message
        message = db.session.query(Message).order_by(
            Message.post_date.desc()).first()

        assert message is not None
        assert message.content == content
        mock_socketio_emit.asssert_called_once_with(
            recipient, {"from": 1, "content": content})


def test_api_message_empty_message(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_socketio_emit = mocker.patch("app.views.api.socketio.emit")
        recipient = 'c6a04d0809b7498fb7b8bcb6369e2218'
        content = ''
        data = {'recipient': recipient,
                'content': content}
        response = client.post(
            "/api/message", data=json.dumps(data), content_type='application/json')

        assert response.is_json
        assert "result" in response.json.keys()
        assert response.json["result"] == 'error'
        assert response.status_code == 400

        from app.models import Message
        message = db.session.query(Message).order_by(
            Message.post_date.desc()).first()

        assert message is None or message.content != content
        assert mock_socketio_emit.call_count == 0


def test_api_message_bad_recipient(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_socketio_emit = mocker.patch("app.views.api.socketio.emit")
        recipient = 'surely_bad'
        content = 'test'
        data = {'recipient': recipient,
                'content': content}
        response = client.post(
            "/api/message", data=json.dumps(data), content_type='application/json')

        assert not response.is_json
        assert response.status_code == 404

        from app.models import Message
        message = db.session.query(Message).order_by(
            Message.post_date.desc()).first()

        assert message is None or message.content != content
        assert mock_socketio_emit.call_count == 0


def test_api_unread_messages(client, mocker):
    mock_socketio_emit = mocker.patch("app.views.api.socketio.emit")
    previous_unread = 0
    new_messages = 3

    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
        response = client.get("/api/messages/unread",
                              content_type='application/json')
        previous_unread = json.loads(response.data)['unread']

        response = client.post(
            "login", data={"email": "test1@bazaragh.pl", "password": "test"})
        for _ in range(new_messages):
            recipient_admin = 'f8084f5d0fb04ab5b0baeccbde7a83a8'
            content = 'test'
            data = {'recipient': recipient_admin,
                    'content': content}
            response = client.post(
                "/api/message", data=json.dumps(data), content_type='application/json')

        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})

    with client:
        curent_unread = client.get(
            "/api/messages/unread", content_type='application/json').json['unread']
        assert curent_unread - previous_unread == new_messages


def test_set_user_offer_rating(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        offer_id = 84
        customer_id = 1

        rating = 2
        data = {'rating': rating}
        response = client.post(
            f"/api/offer/{offer_id}/rating", data=json.dumps(data), content_type='application/json')

        assert response.is_json
        assert "result" in response.json.keys()
        assert response.json["result"] == 'success'

        from app.models import OfferScore
        offer_score = db.session.query(OfferScore).filter_by(
            offer=offer_id, customer=customer_id).one_or_none()

        assert offer_score is not None
        assert offer_score.score == rating

        rating = 4
        data = {'rating': rating}
        response = client.post(
            f"/api/offer/{offer_id}/rating", data=json.dumps(data), content_type='application/json')

        assert response.is_json
        assert "result" in response.json.keys()
        assert response.json["result"] == 'success'

        offer_score = db.session.query(OfferScore).filter_by(
            offer=offer_id, customer=customer_id).one_or_none()

        assert offer_score is not None
        assert offer_score.score == rating


def test_set_user_offer_rating_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        offer_id = 11111111111
        rating = 2
        data = {'rating': rating}

        response = client.post(
            f"/api/offer/{offer_id}/rating", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 404


def test_get_user_offer_rating_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        offer_id = 11111111111
        rating = 2
        data = {'rating': rating}

        response = client.get(f"/api/offer/{offer_id}/rating")

        assert response.status_code == 404


def test_get_user_offer_rating_not_authenticated(client, mocker):
    with client:
        offer_id = 84
        response = client.get(f"/api/offer/{offer_id}/rating")
        assert response.is_json
        assert "rating" in response.json.keys()
        assert response.json["rating"] == 0


def test_get_user_offer_rating(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        offer_id = 84
        customer_id = 1
        response = client.get(f"/api/offer/{offer_id}/rating")
        assert response.is_json
        assert "rating" in response.json.keys()
        assert response.json["rating"] == 0

        rating = 2
        data = {'rating': rating}
        response = client.post(
            f"/api/offer/{offer_id}/rating", data=json.dumps(data), content_type='application/json')

        response = client.get(f"/api/offer/{offer_id}/rating")
        assert response.is_json
        assert "rating" in response.json.keys()
        assert response.json["rating"] == rating


def test_set_user_author_rating(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        customer_id = 1
        author_id = 26
        rating = 2
        data = {'rating': rating}
        response = client.post(
            f"/api/offer/{author_id}/author-rating", data=json.dumps(data), content_type='application/json')

        assert response.is_json
        assert "result" in response.json.keys()
        assert response.json["result"] == 'success'

        from app.models import UserScore
        user_score = db.session.query(UserScore).filter_by(
            seller=author_id, customer=customer_id).one_or_none()

        assert user_score is not None
        assert user_score.score == rating

        rating = 4
        data = {'rating': rating}
        response = client.post(
            f"/api/offer/{author_id}/author-rating", data=json.dumps(data), content_type='application/json')

        assert response.is_json
        assert "result" in response.json.keys()
        assert response.json["result"] == 'success'

        user_score = db.session.query(UserScore).filter_by(
            seller=author_id, customer=customer_id).one_or_none()

        assert user_score is not None
        assert user_score.score == rating


def test_set_user_author_rating_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        author_id = 11111111111
        rating = 2
        data = {'rating': rating}

        response = client.post(
            f"/api/offer/{author_id}/author-rating", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 404


def test_get_user_author_rating_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        author_id = 11111111111

        response = client.get(f"/api/offer/{author_id}/author-rating")

        assert response.status_code == 404


def test_get_user_author_rating_not_authenticated(client, mocker):
    with client:
        author_id = 26
        response = client.get(f"/api/offer/{author_id}/author-rating")
        assert response.is_json
        assert "rating" in response.json.keys()
        assert response.json["rating"] == 0


def test_get_user_author_rating(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        author_id = 26
        response = client.get(f"/api/offer/{author_id}/author-rating")
        assert response.is_json
        assert "rating" in response.json.keys()
        assert response.json["rating"] == 0

        rating = 2
        data = {'rating': rating}
        response = client.post(
            f"/api/offer/{author_id}/author-rating", data=json.dumps(data), content_type='application/json')

        response = client.get(f"/api/offer/{author_id}/author-rating")
        assert response.is_json
        assert "rating" in response.json.keys()
        assert response.json["rating"] == rating
