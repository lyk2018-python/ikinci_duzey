# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Sat Jul 28 16:45:13 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 245)
        MainWindow.setMinimumSize(QtCore.QSize(376, 245))
        MainWindow.setMaximumSize(QtCore.QSize(376, 245))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.yedi = QtWidgets.QPushButton(self.centralwidget)
        self.yedi.setObjectName("yedi")
        self.gridLayout.addWidget(self.yedi, 3, 0, 1, 1)
        self.bir = QtWidgets.QPushButton(self.centralwidget)
        self.bir.setObjectName("bir")
        self.gridLayout.addWidget(self.bir, 5, 0, 1, 1)
        self.nokta = QtWidgets.QPushButton(self.centralwidget)
        self.nokta.setObjectName("nokta")
        self.gridLayout.addWidget(self.nokta, 6, 1, 1, 1)
        self.bes = QtWidgets.QPushButton(self.centralwidget)
        self.bes.setObjectName("bes")
        self.gridLayout.addWidget(self.bes, 4, 1, 1, 1)
        self.kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet.setObjectName("kaydet")
        self.gridLayout.addWidget(self.kaydet, 1, 0, 1, 1)
        self.pac = QtWidgets.QPushButton(self.centralwidget)
        self.pac.setObjectName("pac")
        self.gridLayout.addWidget(self.pac, 1, 2, 1, 1)
        self.sil = QtWidgets.QPushButton(self.centralwidget)
        self.sil.setObjectName("sil")
        self.gridLayout.addWidget(self.sil, 0, 4, 1, 1)
        self.sekiz = QtWidgets.QPushButton(self.centralwidget)
        self.sekiz.setObjectName("sekiz")
        self.gridLayout.addWidget(self.sekiz, 3, 1, 1, 1)
        self.dort = QtWidgets.QPushButton(self.centralwidget)
        self.dort.setObjectName("dort")
        self.gridLayout.addWidget(self.dort, 4, 0, 1, 1)
        self.pkapa = QtWidgets.QPushButton(self.centralwidget)
        self.pkapa.setObjectName("pkapa")
        self.gridLayout.addWidget(self.pkapa, 1, 4, 1, 1)
        self.geri = QtWidgets.QPushButton(self.centralwidget)
        self.geri.setObjectName("geri")
        self.gridLayout.addWidget(self.geri, 0, 2, 1, 1)
        self.topla = QtWidgets.QPushButton(self.centralwidget)
        self.topla.setObjectName("topla")
        self.gridLayout.addWidget(self.topla, 6, 4, 1, 1)
        self.iki = QtWidgets.QPushButton(self.centralwidget)
        self.iki.setObjectName("iki")
        self.gridLayout.addWidget(self.iki, 5, 1, 1, 1)
        self.alti = QtWidgets.QPushButton(self.centralwidget)
        self.alti.setObjectName("alti")
        self.gridLayout.addWidget(self.alti, 4, 2, 1, 1)
        self.dokuz = QtWidgets.QPushButton(self.centralwidget)
        self.dokuz.setObjectName("dokuz")
        self.gridLayout.addWidget(self.dokuz, 3, 2, 1, 1)
        self.uc = QtWidgets.QPushButton(self.centralwidget)
        self.uc.setObjectName("uc")
        self.gridLayout.addWidget(self.uc, 5, 2, 1, 1)
        self.sifir = QtWidgets.QPushButton(self.centralwidget)
        self.sifir.setObjectName("sifir")
        self.gridLayout.addWidget(self.sifir, 6, 0, 1, 1)
        self.carp = QtWidgets.QPushButton(self.centralwidget)
        self.carp.setObjectName("carp")
        self.gridLayout.addWidget(self.carp, 4, 4, 1, 1)
        self.bol = QtWidgets.QPushButton(self.centralwidget)
        self.bol.setObjectName("bol")
        self.gridLayout.addWidget(self.bol, 3, 4, 1, 1)
        self.esittir = QtWidgets.QPushButton(self.centralwidget)
        self.esittir.setObjectName("esittir")
        self.gridLayout.addWidget(self.esittir, 6, 2, 1, 1)
        self.cikar = QtWidgets.QPushButton(self.centralwidget)
        self.cikar.setObjectName("cikar")
        self.gridLayout.addWidget(self.cikar, 5, 4, 1, 1)
        self.cikti = QtWidgets.QLineEdit(self.centralwidget)
        self.cikti.setEnabled(False)
        self.cikti.setObjectName("cikti")
        self.gridLayout.addWidget(self.cikti, 0, 0, 1, 2)
        self.unut = QtWidgets.QPushButton(self.centralwidget)
        self.unut.setObjectName("unut")
        self.gridLayout.addWidget(self.unut, 1, 1, 1, 1)
        self.gerigetir = QtWidgets.QPushButton(self.centralwidget)
        self.gerigetir.setObjectName("gerigetir")
        self.gridLayout.addWidget(self.gerigetir, 2, 0, 1, 1)
        self.kare = QtWidgets.QPushButton(self.centralwidget)
        self.kare.setObjectName("kare")
        self.gridLayout.addWidget(self.kare, 2, 1, 1, 1)
        self.karekok = QtWidgets.QPushButton(self.centralwidget)
        self.karekok.setObjectName("karekok")
        self.gridLayout.addWidget(self.karekok, 2, 2, 1, 1)
        self.mod = QtWidgets.QPushButton(self.centralwidget)
        self.mod.setObjectName("mod")
        self.gridLayout.addWidget(self.mod, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.yedi.setText(QtWidgets.QApplication.translate("MainWindow", "7", None, -1))
        self.bir.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.nokta.setText(QtWidgets.QApplication.translate("MainWindow", ".", None, -1))
        self.bes.setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.kaydet.setText(QtWidgets.QApplication.translate("MainWindow", "Kaydet", None, -1))
        self.pac.setText(QtWidgets.QApplication.translate("MainWindow", "(", None, -1))
        self.sil.setText(QtWidgets.QApplication.translate("MainWindow", "Temizle", None, -1))
        self.sekiz.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.dort.setText(QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.pkapa.setText(QtWidgets.QApplication.translate("MainWindow", ")", None, -1))
        self.geri.setText(QtWidgets.QApplication.translate("MainWindow", "⌫", None, -1))
        self.topla.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.iki.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.alti.setText(QtWidgets.QApplication.translate("MainWindow", "6", None, -1))
        self.dokuz.setText(QtWidgets.QApplication.translate("MainWindow", "9", None, -1))
        self.uc.setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.sifir.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.carp.setText(QtWidgets.QApplication.translate("MainWindow", "✕", None, -1))
        self.bol.setText(QtWidgets.QApplication.translate("MainWindow", "÷", None, -1))
        self.esittir.setText(QtWidgets.QApplication.translate("MainWindow", "=", None, -1))
        self.cikar.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.unut.setText(QtWidgets.QApplication.translate("MainWindow", "Unut", None, -1))
        self.gerigetir.setText(QtWidgets.QApplication.translate("MainWindow", "Geri Getir", None, -1))
        self.kare.setText(QtWidgets.QApplication.translate("MainWindow", "X^2", None, -1))
        self.karekok.setText(QtWidgets.QApplication.translate("MainWindow", "√", None, -1))
        self.mod.setText(QtWidgets.QApplication.translate("MainWindow", "Mod", None, -1))
