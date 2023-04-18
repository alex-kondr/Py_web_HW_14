from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_read_root():
    response = client.get("/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}