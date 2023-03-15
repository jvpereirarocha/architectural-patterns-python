def test_add_new_vote(client):
    response = client.post("/api/v1/votes/add")
    assert response.status_code == 201
    data = {"message": "New vote added"}
    assert response.json == data