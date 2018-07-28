from celery import Celery
from bs4 import BeautifulSoup
import requests
import json

app = Celery('background',backend='redis://localhost', broker='amqp://localhost/')

@app.task
def parse():
    html = requests.get("https://projecteuler.net/archives")
    veri = []

    bs = BeautifulSoup(html.text, "html.parser")
    satirlar = bs.find_all("tr")
    
    for satir in satirlar:
        if satir.find("td") != None:
            sutunlar = satir.find_all("td")
            veri.append({
                "Description"   : sutunlar[1].string,
                "Solved By"     : sutunlar[2].string
            })

    json_path = "data.json"
    with open(json_path, "w") as f:
        json.dump(veri, f)

    return veri