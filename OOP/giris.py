import json
from pprint import pprint

class Kisi:
    ad = "default"
    soyad = ""
    yas = 0

    def __init__(self, isim, soyisim, yasi):
        self.ad = isim
        self.soyad = soyisim
        self.yas = yasi

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, ensure_ascii=False)

    def bilgi_yazdir(self):
        print("Ad    : " + self.ad)
        print("Soyad : " + self.soyad)
        print("Yas   : " + str(self.yas))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, ensure_ascii=False)

    @staticmethod
    def yazdir():
        print("Hello World")

s = Kisi("serhat", "sönmez", 27)
s.bilgi_yazdir()

print(s.to_json())


liste = []
for k in range(1,6):
    nesne = Kisi(str(k) + ".kisi", str(k) + "soyad", k+5)
    liste.append(nesne.to_json())

pprint(liste)

# k = Kisi()
# k.ad = "Serhat"
# k.soyad = "Sönmez"
# k.yas = 27
# 
# k.bilgi_yazdir()
# 
# Kisi.yazdir()
# 
# Kisi.ad = "Python"
# print(Kisi.ad)
# 
# z = Kisi()
# z.ad = "Ahmet"
# z.bilgi_yazdir()

