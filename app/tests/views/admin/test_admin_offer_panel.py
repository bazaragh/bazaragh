def test_img_in_offer_details(client):
    login = "admin@bazaragh.pl"
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": login, "password": "test"})

    response = client.get("/admin/")
    assert response.status_code == 200
    assert f"Zalogowano do panelu administratora jako {login}" in response.text

    response = client.get("/admin/offer/details/?id=84&url=%2Fadmin%2Foffer%2F")
    assert response.status_code == 200
    assert "<img" in response.text
