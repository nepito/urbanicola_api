from fastapi import FastAPI
import json
import pandas as pd
from pydantic import BaseModel


class Item(BaseModel):
    a: list[int]
    b: list[int]
    c: list[bool]

item = Item(**{"a":[0], "b":[0], "c":[False]})
expenses = pd.read_csv("./data/gastos.csv")
f = open("./data/players.json")
players = json.load(f)

app = FastAPI()


@app.get("/v1")
def dummy_request():
    return {"Hello": "World"}


@app.get("/make_add")
def make_add():
    return {"add": 4 + 6}


@app.get("/v1/players")
def get_player():
    return players["response"]


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