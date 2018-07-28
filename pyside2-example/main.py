from PySide2 import QtCore, QtGui, QtWidgets

from untitled import Ui_MainWindow

cikti_default_css = "#cikti{ color : black; }"
cikti_hata_css = "#cikti{background-color: red; color : white; }"


class CustomWindow(Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.islem = []
        self.hafiza = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.cikti.setStyleSheet(cikti_default_css)
        self.bol.setStyleSheet("#bol{ background-color: cyan; }")
        self.carp.setStyleSheet("#carp{ background-color: cyan; }")
        self.cikar.setStyleSheet("#cikar{ background-color: cyan; }")
        self.topla.setStyleSheet("#topla{ background-color: cyan; }")
        self.mod.setStyleSheet("#mod{ background-color: cyan; }")
        self.karekok.setStyleSheet("#karekok{ background-color: cyan; }")
        self.kare.setStyleSheet("#kare{ background-color: cyan; }")
        self.pac.setStyleSheet("#pac{ background-color: lightblue; }")
        self.pkapa.setStyleSheet("#pkapa{ background-color: lightblue; }")
        self.kaydet.setStyleSheet("#kaydet{ background-color: #FF8888; }")
        self.gerigetir.setStyleSheet("#gerigetir{ background-color: #FF8888; }")
        self.unut.setStyleSheet("#unut{ background-color: #FF8888; }")
        self.sil.setStyleSheet("#sil{ background-color: magenta; }")
        self.geri.setStyleSheet("#geri{ background-color: magenta; }")
        self.esittir.setStyleSheet("#esittir{ background-color: yellow; }")

        QtCore.QObject.connect(self.sil, QtCore.SIGNAL("clicked()"), self.temizle)
        QtCore.QObject.connect(self.geri, QtCore.SIGNAL("clicked()"), self.geri_sil)
        QtCore.QObject.connect(self.esittir, QtCore.SIGNAL("clicked()"), self.hesapla)
        QtCore.QObject.connect(self.kaydet, QtCore.SIGNAL("clicked()"), self.kaydet_methodu)
        QtCore.QObject.connect(self.gerigetir, QtCore.SIGNAL("clicked()"), self.gerigetir_methodu)
        QtCore.QObject.connect(self.unut, QtCore.SIGNAL("clicked()"), self.unut_methodu)
        degerler = {
            self.sifir: "0",
            self.bir: "1",
            self.iki: "2",
            self.uc: "3",
            self.dort: "4",
            self.bes: "5",
            self.alti: "6",
            self.yedi: "7",
            self.sekiz: "8",
            self.dokuz: "9",
            self.bol: "/",
            self.carp: "*",
            self.cikar: "-",
            self.topla: "+",
            self.nokta: ".",
            self.mod: "%",
            self.karekok: "**(1/2)",
            self.kare: "**2",
            self.pac: "(",
            self.pkapa: ")",
        }
        for key, value in degerler.items():
            QtCore.QObject.connect(key, QtCore.SIGNAL("clicked()"), self.ekle(value))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ekle(self, n):
        def _ekleme():
            for i in n:
                self.islem.append(i)
            self.cikti.setText(self.get_gosterim())
            self.cikti.setStyleSheet(cikti_default_css)

        return _ekleme

    def get_gosterim(self):
        yeni_gosterim = []
        for i in self.islem:
            if i == "*":
                if yeni_gosterim and yeni_gosterim[-1] == "✕":
                    yeni_gosterim.pop(-1)
                    yeni_gosterim.append("^")
                else:
                    yeni_gosterim.append("✕")
            elif i == "/":
                if yeni_gosterim and yeni_gosterim[-1] == "÷":
                    yeni_gosterim.pop(-1)
                    yeni_gosterim.append("//")
                else:
                    yeni_gosterim.append("÷")
            elif i == "%":
                yeni_gosterim.append("MOD")
            else:
                yeni_gosterim.append(i)

        return " ".join(yeni_gosterim)

    def geri_sil(self):
        if self.islem:
            self.islem.pop(-1)
        self.cikti.setText(self.get_gosterim())
        self.cikti.setStyleSheet(cikti_default_css)

    def hesapla(self):
        islem = "".join(self.islem)
        try:
            sonuc = str(eval(islem))
        except SyntaxError:
            self.cikti.setStyleSheet(cikti_hata_css)
            self.cikti.setText("Malformed expression")
            return
        except ZeroDivisionError:
            self.cikti.setStyleSheet(cikti_hata_css)
            self.cikti.setText("Division by zero is undefined")
            return
        else:
            self.cikti.setStyleSheet(cikti_default_css)
        if (int(float(sonuc)) == float(sonuc)):
            sonuc = str(int(float(sonuc)))
        self.cikti.setText(sonuc)

        self.islem = [sonuc]

    def temizle(self):
        self.cikti.setStyleSheet(cikti_default_css)
        self.cikti.clear()
        self.islem = []

    def kaydet_methodu(self):
        self.hesapla()
        sonuc = self.cikti.text()
        if sonuc:
            self.hafiza = sonuc
        else:
            self.hafiza = None

    def gerigetir_methodu(self):
        if self.hafiza is not None:
            self.islem.append(self.hafiza)
        self.cikti.setText(self.get_gosterim())
        self.cikti.setStyleSheet(cikti_default_css)

    def unut_methodu(self):
        self.hafiza = None
        self.temizle()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CustomWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
