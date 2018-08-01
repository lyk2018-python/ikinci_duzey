import re

import bs4
import requests

import tfidf


def _indir(i):
    user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    data = requests.get("https://eksisozluk.com/python--109286?p={}".format(i), headers=user_agent)
    soup = bs4.BeautifulSoup(data.text, "lxml")
    base = soup.find("ul", attrs={"id": "entry-item-list"})
    return [x.text.strip() for x in base.find_all("div", attrs={"class": "content"})]


def frekansla_beni_scotty(entry, butun_entryler):
    return {word: (len(word), tfidf.tfidf(word, entry, butun_entryler)) for word in re.findall(r"[a-zA-Z]+", entry)}
