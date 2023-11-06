from fastapi import FastAPI
import json


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/make_add")
def make_add():
    return {"add": 4 + 6}
