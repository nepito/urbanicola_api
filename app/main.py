from fastapi import FastAPI
import json
import pandas as pd

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
