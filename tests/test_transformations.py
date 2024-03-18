from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

gasto = {
    "date": ["2024-03-18"],
    "mount": [0],
    "type": ["string"],
    "concept": ["string"],
    "subtype": ["string"],
    "area": ["string"],
    "how_many": [0],
    "provider": ["string"],
    "factura": [True],
    "payment_type": ["string"],
    "bank_count": ["string"],
    "description": ["string"],
}


def test_read_main():
    response = client.post("/v1/spent/", json=gasto)
    assert response.status_code == 200
    assert response.json()["description"] == ["string"]
