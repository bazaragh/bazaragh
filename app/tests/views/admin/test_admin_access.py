def test_admin_access_with_admin_user(client):
    login = "admin@bazaragh.pl"
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": login, "password": "test"})

    response = client.get("/admin/")
    assert response.status_code == 200
    assert f"Zalogowano do panelu administratora jako {login}" in response.text


def test_admin_access_with_default_user(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "test2@bazaragh.pl", "password": "test"})

    response = client.get("/admin/")
    assert response.status_code == 200
    assert "Panel administratora jest dostępny tylko dla Moderatorów i Administratorów." in response.text \
           or "Nie posiadasz uprawnień Moderatora lub Administratora." in response.text


def test_admin_access_with_moderator(client):
    login = "test1@bazaragh.pl"
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": login, "password": "test"})

    response = client.get("/admin/")
    assert response.status_code == 200
    assert f"Zalogowano do panelu administratora jako {login}" in response.text
