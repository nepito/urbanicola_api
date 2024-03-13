import datetime
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel


class Gasto(BaseModel):
    date: list[datetime.date]
    mount: list[float]
    type: list[str]
    concept: list[str]
    subtype: list[str]
    area: list[str]
    how_many: list[float]
    provider: list[str]
    factura: list[bool]
    payment_type: list[str]
    bank_count: list[str]
    description: list[str]


description = """
Urbanícola API 🦈
"""


app = FastAPI(
    title="Urbanicola",
    description=description,
    summary="API about Urbanícola money.",
    version="0.1.0",
    contact={
        "name": "NIES",
        "url": "https://github.com/niesfutbol",
        "email": "nepo@nies.futbol",
    },
    license_info={
        "name": "AGPL-3.0 license",
        "url": "https://github.com/nepito/urbanicola_api/blob/develop/LICENSE",
    },)


@app.post("/v1/spent")
def add_spent(spent: Gasto):
    data_base = "./data/spents.csv"
    test_data = pd.read_csv(data_base)
    df_row = pd.DataFrame(spent.dict())
    new_df = pd.concat([test_data, df_row])
    new_df.to_csv(data_base, index=False)
    return spent.dict()
