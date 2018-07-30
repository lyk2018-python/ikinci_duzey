from typing import List, Tuple, Union

import requests
import bs4
import tabulate
import statistics
import pytemperature
import os
import datetime
import lxml.html

exit_code: int = 0
"""
    0 Success
    1 General Error
    20 General Connection Error
    21 Connection Error on goc
    22 Connection Error on weather
    23 Connection Error on itugnu
    23 Connection Error on beyazperde
"""

T_Row = List[Union[str, int, float]]
T_Rows = List[T_Row]


def set_exit_code(number: int):
    global exit_code
    if 20 <= exit_code < 30 and 20 <= number < 30:
        number = 20

    exit_code = number


def get_header_and_data(soup: bs4.BeautifulSoup) -> Tuple[List[str], List[T_Row]]:
    basliklar = []
    satirlar = []

    for sira, satir in enumerate(soup.find("table").find_all("tr")):
        if sira in (0, 2):
            continue

        for sutun in satir.find_all("th"):
            basliklar.append(sutun.text)

        sutunlar = []
        for sutun in satir.find_all("td"):
            sutunlar.append(sutun.text)
        if sutunlar:
            satirlar.append(sutunlar)

    return basliklar, satirlar


def cast_data(row_data: List[T_Row]) -> List[T_Row]:
    yeni_satirlar = []

    for satir in row_data:
        yeni_satir = list(satir)

        for sutun_sirasi in range(1, 5):
            veri = yeni_satir[sutun_sirasi]
            yeni_satir[sutun_sirasi] = int(veri.replace(",", ""))

        yeni_satir[5] = float(yeni_satir[5])
        yeni_satirlar.append(yeni_satir)

    return yeni_satirlar


def get_calculated_rows(row_data: T_Rows) -> Tuple[T_Row, T_Row, T_Row]:
    total_population = []
    in_migration = []
    out_migration = []

    for satir in row_data:
        total_population.append(satir[1])
        in_migration.append(satir[2])
        out_migration.append(satir[3])

    maksimum_satir = ["Maksimum", max(total_population), max(in_migration), max(out_migration), 0, 0.0]
    ortalama_satir = ["Ortalama", statistics.mean(total_population), statistics.mean(in_migration),
                      statistics.mean(out_migration), 0, 0.0]
    minimum_satir = ["Minimum", min(total_population), min(in_migration), min(out_migration), 0, 0.0]

    return maksimum_satir, ortalama_satir, minimum_satir


def get_formatted_rows(row_data):
    formatli_satirlar = []
    for satir in row_data:
        formatli_satirlar.append([
            satir[0],
            "{:d}".format(int(satir[1])),
            "{:d}".format(int(satir[2])),
            "{:d}".format(int(satir[3])),
            "{:d}".format(int(satir[4])),
            "{:.3f}".format(satir[5]),
        ])
    return formatli_satirlar


def get_goc_data(pp=False):
    base_url = "http://itu17-a3-asocia.herokuapp.com/"
    try:
        anasayfa_response = requests.get(base_url)
    except requests.ConnectionError as e:
        set_exit_code(21)
        if not os.getenv("FAIL_SILENTLY", ""):
            print(base_url, "|", e)
            raise
        else:
            return

    anasayfa_soup = bs4.BeautifulSoup(anasayfa_response.text, "lxml")

    basliklar, ham_satirlar = get_header_and_data(anasayfa_soup)
    cast_satirlar = cast_data(ham_satirlar)
    ortalama_satirlar = get_calculated_rows(cast_satirlar)

    for row in reversed(ortalama_satirlar):
        cast_satirlar.insert(0, row)

    if pp:
        formatli_satirlar = get_formatted_rows(cast_satirlar)
        guzel_tablo = tabulate.tabulate(formatli_satirlar, headers=basliklar, tablefmt="fancy_grid")
        print(anasayfa_soup.find(class_="title").text)
        print(guzel_tablo)
    else:
        return [{baslik: deger for baslik, deger in zip(basliklar, satir)} for satir in cast_satirlar]


def get_weather_response():
    base_url = "https://www.yahoo.com/news/weather"
    try:
        hava_response = requests.get(base_url)
    except requests.ConnectionError as e:
        set_exit_code(22)
        if not os.getenv("FAIL_SILENTLY", ""):
            print(base_url, "|", e)
            raise
        else:
            return
    return hava_response


def get_weather_data_xpath(hava_response, pp=False):
    element_tree = lxml.html.fromstring(hava_response.text)
    root_element_xpath = "/html/body/div[1]/div/div[1]/div/div[4]/div[1]" \
                         "/div/div[2]/div/div/div/div/section[2]/div/div[3]"

    temp_elements = element_tree.xpath(root_element_xpath + "/span[1]")
    deg_elements = element_tree.xpath(root_element_xpath + "/div/button[1]")

    if temp_elements:
        temp_element = temp_elements[0]
    else:
        raise ValueError("Sıcaklık elementini bulamadık")

    if deg_elements:
        deg_element = deg_elements[0]
    else:
        raise ValueError("Ölçek elementini bulamadık")

    derece = temp_element.text
    olcek = deg_element.text

    if olcek.lower() == "f":
        celcius_derece = int(pytemperature.f2c(int(derece)))
    elif olcek.lower() == "c":
        celcius_derece = int(derece)
    else:
        raise ValueError("Yahoo'nun gösterdiği sıcaklık ölçeği celcius ya da fahreneit değil")

    if pp:
        import sys
        if sys.version_info[:2] >= (3, 6):
            print(f"{celcius_derece:d}C°")
        else:
            print("{:d} C°".format(celcius_derece))
    else:
        return {"degree": celcius_derece, "scale": "C"}


def get_weather_data(hava_response, pp=False):
    hava_soup = bs4.BeautifulSoup(hava_response.text, "html.parser")

    now_soup = hava_soup.find(class_="temperature").find(class_="now")

    derece = now_soup.find("span").text
    olcek = now_soup.find(class_="unit-control").find("button").text

    if olcek.lower() == "f":
        celcius_derece = int(pytemperature.f2c(int(derece)))
    elif olcek.lower() == "c":
        celcius_derece = int(derece)
    else:
        raise ValueError("Yahoo'nun gösterdiği sıcaklık ölçeği celcius ya da fahreneit değil")

    if pp:
        import sys
        if sys.version_info[:2] >= (3, 6):
            print(f"{celcius_derece:d}C°")
        else:
            print("{:d} C°".format(celcius_derece))
    else:
        return {"degree": derece, "scale": "C"}


def get_itugnu_data(pp=False):
    base_url = "https://itugnu.org/tr/lectures/"

    try:
        itugnu_response = requests.get(base_url)
    except requests.ConnectionError as e:
        set_exit_code(23)
        if not os.getenv("FAIL_SILENTLY", ""):
            print(base_url, "|", e)
            raise
        else:
            return

    itugnu_soup = bs4.BeautifulSoup(itugnu_response.text, "lxml")
    etkinlikler = {}
    for container in itugnu_soup.find_all(class_="portfolio-caption"):
        h4 = container.find("h4")

        if "fa-star" in h4.find("i").attrs["class"]:
            durum = True
        else:
            durum = False

        etkinlikler[h4.text.strip()] = durum

    if pp:
        for etk, aciklik in etkinlikler.items():
            print(etk, "|", "Açık" if aciklik else "Kapalı")
    else:
        return [{"etkinlik": etkinlik, "durum": durum} for etkinlik, durum in etkinlikler.items()]


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


def get_beyazperde_data(sayi=5, pp=False):
    bugun = datetime.date.today()
    bu_hafta_pazartesi = bugun - datetime.timedelta(days=bugun.weekday())

    if bugun.weekday() > 4:
        bu_hafta_pazartesi = bugun + datetime.timedelta(days=7)

    bu_hafta_cuma = bu_hafta_pazartesi + datetime.timedelta(days=4)
    onceki_bes_cuma = [bu_hafta_cuma - datetime.timedelta(days=7 * i) for i in range(1, 1 + sayi)]
    haftalik_filmler = []
    for sira, gun in enumerate([bu_hafta_cuma] + onceki_bes_cuma):
        base_url = "http://www.beyazperde.com/filmler/takvim/?week={}".format(gun.isoformat())

        try:
            beyazperde_response = requests.get(base_url)
        except requests.ConnectionError as e:
            set_exit_code(24)
            if not os.getenv("FAIL_SILENTLY", ""):
                print(base_url, "|", e)
                raise
            else:
                return

        beyazperde_soup = bs4.BeautifulSoup(beyazperde_response.text, "lxml")

        data_box = beyazperde_soup.find_all(class_="data_box")
        filmler = []
        for datum in data_box:
            if datum.find(class_="note") is not None:
                skor = float(datum.find(class_="note").text.replace(",", "."))
            else:
                skor = 0.0

            filmler.append(Film(datum.find("h2").text.strip(), skor))

        haftalik_filmler.append(({"hafta": gun, "filmler": list(sorted(filmler))}))

    if pp:
        for sira, veri in enumerate(haftalik_filmler):
            if sira == 0:
                print("###Bu Haftanın Filmleri")
            else:
                print("###Haftanın Filmleri ({})".format(veri["hafta"].isoformat()))
            print(*[str(film) for film in veri["filmler"]], sep="\n")
            print("-" * 39)
    else:
        return [
            {
                "hafta": veri["hafta"].isoformat(),
                "filmler": [
                    {
                        "isim": film.isim,
                        "skor": film.skor
                    }
                    for film in veri["filmler"]
                ]
            }
            for veri in haftalik_filmler
        ]


def compare_xpath_bs4():
    import textwrap
    setup_stmt = textwrap.dedent("""
        from __main__ import get_weather_data_xpath, get_weather_data, get_weather_response
        response = get_weather_response()
        """)
    import sys
    import os

    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    iteration = 1000
    import timeit

    x1 = timeit.timeit(stmt="get_weather_data_xpath(response)", setup=setup_stmt, number=iteration)
    x2 = timeit.timeit(stmt="get_weather_data(response)", setup=setup_stmt, number=iteration)

    sys.stdout = old_stdout
    print("{} loops, average: {:.3f} sec per loop".format(iteration, x1 / iteration))
    print("{} loops, average: {:.3f} sec per loop".format(iteration, x2 / iteration))


if __name__ == '__main__':
    get_goc_data(pp=True)
    print("-" * 79)
    get_weather_data(get_weather_response(), pp=True)
    print("-" * 79)
    get_weather_data_xpath(get_weather_response(), pp=True)
    print("-" * 79)
    get_itugnu_data(pp=True)
    print("-" * 79)
    get_beyazperde_data(pp=True)
    print("-" * 79)
    compare_xpath_bs4()
    print("-" * 79)

    exit(exit_code)
