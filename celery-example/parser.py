from celery import Celery
import json
import os

app = Celery(__name__, backend="redis://localhost", broker="amqp://localhost")


@app.task
def parse(gelenVeri, dosya_adi="data.json"):
    dic = {
        "Kelime": gelenVeri,
        "Parsed": gelenVeri.split(" ")
    }

    if not os.path.exists("data.json"):
        with open(dosya_adi, "w") as f:
            json_data = {"data": []}
            json.dump(json_data, f)

    with open(dosya_adi, "r") as f:
        data = json.load(f)
        data["data"].append(dic)

    with open(dosya_adi, "w") as f:
        json.dump(data, f)

    return dosya_adi


@app.task
def get_parsed(dosya_adi="data.json"):
    with open(dosya_adi, "r") as f:
        return json.load(f)["data"]
