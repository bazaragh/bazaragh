import json


def test_loading_chat(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "test2@bazaragh.pl", "password": "test"})
    response = client.get("/messages/")
    assert response.status_code == 200
    response = client.get("/messages/8")
    assert response.status_code == 200


def test_sending_message(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "test2@bazaragh.pl", "password": "test"})

    fs_uniquifier = "f8084f5d0fb04ab5b0baeccbde7a83a8"

    data = {
        'recipient': fs_uniquifier,
        'content': 'hejka'
    }
    response = client.post("/api/message", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200


def test_unread(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "test1@bazaragh.pl", "password": "test"})

        response = client.get("/api/messages/unread")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['unread'] == 7


def test_long_conversation(client):
    # Send message
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "test2@bazaragh.pl", "password": "test"})

    fs_uniquifier = "f8084f5d0fb04ab5b0baeccbde7a83a8"

    data = {
        'recipient': fs_uniquifier,
        'content': 'hejka admin'
    }
    response = client.post("/api/message", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200

    # Logout
    response = client.get("/logout")
    assert response.status_code == 302

    # Login with new user
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})

    # Check unread messages
    response = client.get("/api/messages/unread")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['unread'] == 1

    # Read message
    response = client.get("/messages/1")
    assert "hejka admin" in response.text
