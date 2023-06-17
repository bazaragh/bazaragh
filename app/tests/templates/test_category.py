def test_category(client, captured_templates):
    with client:
        cat_names = ["Moda", "Elektronika", "Edukacja", "Sport"]
        for idx, cat_name in enumerate(cat_names):
            response = client.get("/category/" + str(cat_name))
            assert response.status_code == 200
            assert len(captured_templates) == idx + 1
            template, context = captured_templates[idx]
            assert template.name == "category_view.jinja"
            assert context["category_name"] == cat_name
            assert context["pagination"].page == 1

def test_category_pagination(client, captured_templates):
    '''There has to be at least OFFERS_PER_PAGE+1 items in cat_names
    for this test to pass.'''
    with client:
        cat_names = ["Moda"]
        for idx, cat_name in enumerate(cat_names):
            response = client.get("/category/" + str(cat_name) + "/2")
            assert response.status_code == 200
            assert len(captured_templates) == idx + 1
            template, context = captured_templates[idx]
            assert template.name == "category_view.jinja"
            assert context["category_name"] == cat_name
            assert context["pagination"].page == 2