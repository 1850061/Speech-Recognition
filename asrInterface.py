# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QAction, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 462)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # 先坐标，后长宽
        self.label_3.setGeometry(QtCore.QRect(60, 240, 201, 56))
        font = self.setFont("Calibri", 14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 201, 21))
        font = self.setFont("Calibri", 14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(70, 10, 161, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 120, 214, 80))
        font = self.setFont("Calibri", 14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 201, 80))
        font = self.setFont("Calibri", 14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.label_sayWhat = QtWidgets.QLabel(self.centralwidget)
        self.label_sayWhat.setGeometry(QtCore.QRect(60, 400, 201, 26))
        font = self.setFont("Calibri", 14)
        self.label_sayWhat.setFont(font)
        self.label_sayWhat.setStyleSheet("color: green;")
        self.label_sayWhat.setWordWrap(True)
        self.label_sayWhat.setObjectName("label_sayWhat")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("color: green;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "语音助手"))
        self.label_3.setText(_translate("MainWindow", "1. 说\"音乐\"来听音乐"))
        self.label_2.setText(_translate("MainWindow", "你可以:"))
        self.label.setText(_translate("MainWindow", "您好？有什么可以帮到您的吗？"))
        self.label_4.setText(_translate("MainWindow", "2. 说 \"笔记本\"来打开笔记本"))
        self.label_sayWhat.setText(_translate("MainWindow", "您没说话"))


    # 添加字体设置函数
    def setFont(self, typeface, fontSize) -> QtGui.QFont():
        font = QtGui.QFont()
        font.setFamily(typeface)
        font.setPointSize(fontSize)
        return font

    def updateSayWhat(self, say):
        self.updateBar("")
        _translate = QtCore.QCoreApplication.translate
        self.label_sayWhat.setText(_translate("MainWindow", say))


    def updateBar(self, say):
        self.statusbar.showMessage(say)

