import datetime
from pprint import pprint

import bs4
import requests
from celery import Celery, group

app = Celery(__name__, backend="redis://localhost", broker="amqp://localhost")


class Film:
    def __init__(self, isim, skor):
        self.isim = isim
        self.skor = skor

    def __lt__(self, other):
        if self.skor == other.skor:
            return True if self.isim < other.isim else False
        else:
            return True if self.skor > other.skor else False

    def __str__(self):
        return "{} | {}".format(self.isim, self.skor)


@app.task
def get_tarihler(hafta_sayisi=5):
    bugun = datetime.date.today()
    bu_hafta_pazartesi = bugun - datetime.timedelta(days=bugun.weekday())

    if bugun.weekday() > 4:
        bu_hafta_pazartesi = bugun + datetime.timedelta(days=7)

    bu_hafta_cuma = bu_hafta_pazartesi + datetime.timedelta(days=4)
    haftalar_listesi = [(bu_hafta_cuma - datetime.timedelta(days=7 * i)).isoformat() for i in
                        range(1, 1 + hafta_sayisi)]
    return haftalar_listesi


@app.task(bind=True)
def split_jobs(task, tarihler):
    signature = group(get_hafta.si(t) for t in tarihler)
    task.replace(signature)


@app.task
def get_hafta(tarih):
    base_url = "http://www.beyazperde.com/filmler/takvim/?week={}".format(tarih)

    beyazperde_response = requests.get(base_url)

    beyazperde_soup = bs4.BeautifulSoup(beyazperde_response.text, "lxml")

    data_box = beyazperde_soup.find_all(class_="data_box")
    filmler = []
    for datum in data_box:
        if datum.find(class_="note") is not None:
            skor = float(datum.find(class_="note").text.replace(",", "."))
        else:
            skor = 0.0

        filmler.append(Film(datum.find("h2").text.strip(), skor))

    sirali_filmler = list(sorted(filmler))

    return {"tarih": tarih, "filmler": [{"isim": f.isim, "skor": f.skor} for f in sirali_filmler]}


if __name__ == '__main__':
    result = [get_hafta(hafta) for hafta in get_tarihler()]
    pprint(result)
