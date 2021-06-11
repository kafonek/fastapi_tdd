def test_user_login(client):
    resp1 = client.post("/security/login", data={"username": "test", "password": "test"})
    assert resp1.status_code == 200

    token = resp1.json()["access_token"]

    resp2 = client.get("/user", headers={"Authorization": "Bearer %s" % token})
    assert resp2.status_code == 200
    assert resp2.json() == {"username": "test"}
