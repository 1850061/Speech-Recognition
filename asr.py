from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import pyqtSignal

from asrInterface import Ui_MainWindow
import sys
import time

import speech_recognition as sr

from asrFunction import asrFunction


from saveVoice import saveVoice
from voiceApi import distinguish


# 继承QThread
class Runthread(QtCore.QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self, mywindow):
        super(Runthread, self).__init__()
        self.mw = mywindow

    def __del__(self):
        self.wait()

    def run(self):
        speech_interaction(self.mw)
        # self._signal.emit("run")  # 信号发送


class myWindow(QtWidgets.QMainWindow):
    text = ""

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def speech_interaction(mywindow):
    # obtain audio from the microphone
    # 从麦克风记录数据
    while True:
        mywindow.ui.updateSayWhat("录音中...")
        saveVoice()
        mywindow.ui.updateSayWhat("解析中...")
        voice = distinguish()
        print("You said: {}".format(voice))
        if voice is None:
            mywindow.ui.updateSayWhat("解析失败")
            continue

        if voice == "" or len(voice) < 1:
            mywindow.ui.updateSayWhat("您没说话")
            time.sleep(5)
            continue

        func = asrFunction()

        if voice == "音乐":
            mywindow.ui.updateSayWhat("您说 \"音乐\"")
            func.playMusic("Schnappi")

        elif voice == "笔记本":
            mywindow.ui.updateSayWhat("您说 \"笔记本\"")
            func.openNotepad()
        elif voice == "画画":
            mywindow.ui.updateSayWhat("您说 \"画画\"")
            func.drawPicture()
        elif voice == "关闭":
            mywindow.ui.updateSayWhat("您说 \"关闭\"")
            time.sleep(5)
            sys.exit(app.exec())
        else:
            mywindow.ui.updateSayWhat("您说了 \"" + voice + "\"")
            mywindow.ui.updateBar("我们没有这个功能")
        time.sleep(5)


app = QtWidgets.QApplication([])
application = myWindow()
application.show()


thread = Runthread(application)
thread.start()
sys.exit(app.exec())
