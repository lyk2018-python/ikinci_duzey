# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nontitled.ui',
# licensing of 'nontitled.ui' applies.
#
# Created: Sun Jul 29 19:17:30 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image:url(:/arkaplanlar/IMG_772385.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.giren = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.giren.setObjectName("giren")
        self.verticalLayout.addWidget(self.giren)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cikan = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cikan.setReadOnly(True)
        self.cikan.setObjectName("cikan")
        self.verticalLayout.addWidget(self.cikan)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.buton = QtWidgets.QPushButton(self.centralwidget)
        self.buton.setObjectName("buton")
        self.verticalLayout.addWidget(self.buton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 515, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Girdi", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Çıktı", None, -1))
        self.buton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))

