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
