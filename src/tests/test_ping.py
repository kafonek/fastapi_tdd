def test_ping(client):
    endpoint = "/ping"
    resp = client.get(endpoint)
    assert resp.status_code == 200
    assert resp.json() == {"ping": "pong"}
