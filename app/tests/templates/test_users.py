def test_user_by_id(client, captured_templates):
    with client:
        ids = [1, 8, 11]
        for idx, id in enumerate(ids):
            response = client.get("/user/" + str(id))
            assert response.status_code == 200
            assert len(captured_templates) == idx + 1
            template, context = captured_templates[idx]
            assert template.name == "user_view.jinja"
            assert context["user"].id == id
        
        wrong_ids = [2, 3, 4]
        for idx, id in enumerate(wrong_ids):
            response = client.get("/user/" + str(id))
            assert response.status_code == 404

def test_user_offers(client, captured_templates):
    with client:
        ids = [1, 8, 11]
        for idx, id in enumerate(ids):
            response = client.get("/user/" + str(id) + "/offers")
            assert response.status_code == 200
            assert len(captured_templates) == idx + 1
            template, context = captured_templates[idx]
            assert template.name == "user_offers_view.jinja"
            assert context["user"].id == id
        
        wrong_ids = [2, 3, 4]
        for idx, id in enumerate(wrong_ids):
            response = client.get("/user/" + str(id) + "/offers")
            assert response.status_code == 404