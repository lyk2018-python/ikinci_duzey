"""
İhtiyaç olan untitled dosyası için şu komut ile untitled.ui'den untitled.py oluşturabiliriz

$ pyside2-uic -o untitled.py untitled.ui
"""
from kaynak import qInitResources


import os
from urllib.parse import unquote
import pygame
from PySide2 import QtCore, QtWidgets

from nontitled import Ui_MainWindow


cikti_default_css = "#cikti{ color : black; }"
cikti_hata_css = "#cikti{background-color: red; color : white; }"


class CustomWindow(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {background-image:}")

        self.progressBar.hide()
        QtCore.QObject.connect(self.buton, QtCore.SIGNAL("clicked()"), self.gonder_al)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self.kaydet)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("photoshop.mp3")
        pygame.mixer.music.play()

    def kaydet(self):
        dialog = QtWidgets.QFileDialog()
        folder = dialog.getExistingDirectory()

        text = self.cikan.toPlainText()
        if text:
            with open(os.path.join(folder, "son_data.txt"), "w") as f:
                f.write(text)

    def gonder_al(self):
        import requests
        resp = requests.post("http://51.15.49.65:8080/", data={"giren": self.giren.toPlainText()})
        if resp.status_code == 200:
            text = resp.text
            text = text.strip("------------------------------t")
            headers = []
            body = []
            is_headers = True
            for line in text.splitlines():
                if not line:
                    is_headers = False
                    continue
                elif is_headers:
                    headers.append(line)
                else:
                    body.append(line)
            headers = "\n".join(headers)
            body = unquote("\n".join(body))
            self.progressBar.show()
            import time
            import random
            for i in range(101):
                self.progressBar.setValue(i)
                time.sleep(random.randint(0, 100) / 5000)
            self.progressBar.hide()
            self.cikan.setPlainText("{}\n\n---===≡≡≡İÇERİK≡≡≡===---\n\n{}\n\n---===≡≡≡CD-KEY≡≡≡===---\n\n".format(headers, body))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    qInitResources()
    MainWindow = QtWidgets.QMainWindow()
    ui = CustomWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
