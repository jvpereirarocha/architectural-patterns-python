def test_get_votes(client):
    response = client.get("/api/v1/votes/")
    assert response.status_code == 200
    data = {"message": "Total of votes: 0"}
    assert response.json == data