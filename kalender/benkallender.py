import datetime


def anamenu():
    # isocalendarkisi = input("İsim ver: ")
    # sinif = input("Sınıfını yaz: ")
    cikti = input("Tarih Gir: ")
    y, a, g = cikti.split("-")

    bugun = datetime.date.today()
    yeni = datetime.date(int(y), int(a), int(g))

    print(bugun.isoformat())
    print(yeni.isoformat())
    # print(kisi + sinif + "Selam")
    print("Hafta Sayısı: {}".format(yeni.isocalendar()[1]), cikti)
    print("EU Standart: {}/{}/{}".format(yeni.day, yeni.month, yeni.year))
    return yeni


def anamenu2():
    print("Bugünün Tarihi: ", datetime.date.today().isoformat()),
    yeni_tarih = input("Yeni Tarih Giriniz (iso8601) > ")
    girilen_tarih = datetime.datetime.strptime(yeni_tarih, "%Y-%m-%d").date()
    print("Girilen Tarih", girilen_tarih.isoformat())
    print("Hafta Sayısı:", girilen_tarih.isocalendar()[1])
    print("EU Standart:", datetime.datetime.strftime(girilen_tarih, "%-d/%-m/%Y"))
    return girilen_tarih


if __name__ == '__main__':
    anamenu()
