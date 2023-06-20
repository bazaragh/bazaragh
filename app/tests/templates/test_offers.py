from app.app import db


def test_redirect_when_not_logged_in(client):
    '''When user isn't logged in they should be redirected to login page'''
    with client:
        urls = [
            "/user/offer/edit/89",
            "/user/offer/add",
            "/user/offer/delete/89",
            "/user/offer/add-favourite/89",
            "/user/offer/delete-favourite/89",
        ]

        for url in urls:
            response = client.get(url)
            assert response.status_code == 302

            response = client.post(url)
            assert response.status_code == 302


def test_offer_details(client, captured_templates):
    with client:
        offer_ids = [89, 84, 87, 88]
        for idx, offer_id in enumerate(offer_ids):
            response = client.get("/offer/" + str(offer_id))
            assert response.status_code == 200
            assert len(captured_templates) == idx + 1
            template, context = captured_templates[idx]
            assert template.name == "offer/offer.jinja"
            assert context["offer"].id == offer_id


def test_offer_doesnt_exist(client, captured_templates):
    with client:
        offer_ids = [0, 1]
        for idx, offer_id in enumerate(offer_ids):
            response = client.get("/offer/" + str(offer_id))
            assert response.status_code == 404
            assert len(captured_templates) == idx + 1
            template, _ = captured_templates[idx]
            assert template.name == "errors/error.jinja"
