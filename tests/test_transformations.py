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


def test_post_spent():
    response = client.post("/v1/spent/", json=gasto)
    assert response.status_code == 200
    assert response.json()["description"] == ["string"]


ventas = {
    "concept": ["string"],
    "sales_date": ["2024-03-18"],
    "expiration": ["2024-03-18"],
    "status": ["string"],
    "sales_credit": [True],
    "customer": ["string"],
    "prod_serv": ["string"],
    "amount": [6],
    "paid": [6],
    "unit_price": [6],
    "bank_account": ["string"],
    "way_pay": ["string"],
    "sector": ["string"],
    "invoice_folio": [6],
    "date_issue": ["2024-03-18"],
    "final_price": [6],
    "discount": [6],
    "income": [6],
    "product_cost": [6],
}


def test_post_sales():
    response = client.post("/v1/sales/", json=ventas)
    assert response.status_code == 200
    assert response.json()["product_cost"]
