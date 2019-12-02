import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPlainTextEdit
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QTimeEdit
from PyQt5.QtGui import QPixmap
from win10toast import ToastNotifier
import time
from datetime import datetime

class fileush(QWidget):
    def __init__(self, *args):
        super().__init__()

        uic.loadUi('ui_fileush.ui', self)
        self.pushButton.clicked.connect(self.running)

    def running(self):
        toaster = ToastNotifier()
        self.now = datetime.now()
        self.tmf = self.tm.time()
        self.uak = self.tmf.toString()
        self.current_time = self.now.strftime("%H:%M:%S")
        self.seku = self.current_time.split(":")
        self.seku2 = self.uak.split(":")
        self.seknot = 3600 * (int(self.seku2[0])) + (int(self.seku2[1])) * 60
        self.sekcur = 3600 * (int(self.seku[0])) + (int(self.seku[1])) * 60 + (int(self.seku[2]))

        if self.sekcur >= self.seknot:
            self.label_5.setText('ERROR')

        else:
            self.label_5.setText('')
            self.secs = 3600 * (int(self.seku2[0]) - int(self.seku[0])) + 60 * (int(self.seku2[1]) - int(self.seku[1])) - int(self.seku[2])
            self.second_input = self.lineEdit_2.text()
            t = time.sleep(int(self.secs))
            toaster.show_toast(self.second_input)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = fileush()
    ex.show()
    sys.exit(app.exec())