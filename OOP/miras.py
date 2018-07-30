
class Kisi():
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def kisi_bilgi_yazdir(self):
        print("İsim    : " + self.isim)
        print("Soyisim : " + self.soyisim)


class Ogrenci(Kisi):
    def __init__(self, isim, sube):
        super().__init__(isim, "")
        self.sube = sube

    def tum_bilgi_yazdir(self):
        self.kisi_bilgi_yazdir()
        print("Sınıf   : " + self.sube)


class Ogretmen(Kisi):
    def kisi_bilgi_yazdir(self):
        print("Öğretmen bilgileri")
        super().kisi_bilgi_yazdir()


k = Ogrenci("serhat", "505")
k.kisi_bilgi_yazdir()
print()
k.tum_bilgi_yazdir()

print()

x = Ogretmen("umut", "karci")
x.kisi_bilgi_yazdir()


class Ogrencix():
    def __init__(self, isim, soyisim, sube):
        self.isim = isim
        self.soyisim = soyisim
        self.sube = sube

    def kisi_bilgi_yazdir(self):
        print("İsim    : " + self.isim)
        print("Soyisim : " + self.soyisim)

    def tum_bilgi_yazdir(self):
        print("İsim    : " + self.isim)
        print("Soyisim : " + self.soyisim)
        print("Sınıf   : " + self.sube)
