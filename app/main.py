from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel


class Item(BaseModel):
    name: list[str]
    age: list[int]
    client: list[bool]


class Gasto(BaseModel):
    date: list[str]
    mount: list[float]
    type: list[str]
    concept: list[str]
    subtype: list[str]
    area: list[str]
    how_many: list[float]
    provider: list[str]
    factura: list[bool]
    type_pay: list[str]
    bank_count: list[str]
    description: list[str]


expenses = pd.read_csv("./data/gastos.csv")

app = FastAPI()


@app.get("/v1")
def dummy_request():
    return {"Hello": "World"}


@app.get("/make_add")
def make_add():
    return {"add": 4 + 6}


@app.get("/v1/gastos")
def get_expenses():
    return expenses.to_json(orient="records")


@app.post("/v1/item")
def create_item(item: Item):
    test_data = pd.read_csv("./data/test_data.csv")
    df_row = pd.DataFrame(item.dict())
    new_df = pd.concat([test_data, df_row])
    new_df.to_csv("./data/test_data.csv", index=False)
    return item.dict()


@app.post("/v1/spent")
def add_spent(spent: Gasto):
    test_data = pd.read_csv("./data/gastos.csv")
    df_row = pd.DataFrame(spent.dict())
    new_df = pd.concat([test_data, df_row])
    new_df.to_csv("./data/gastos.csv", index=False)
    return spent.dict()
