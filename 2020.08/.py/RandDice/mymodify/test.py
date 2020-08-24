import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from mymodify.dice.user import User
from mymodify.menu import menu
from random import randint
from PyQt5.QtGui import *
from PyQt5 import QtCore

# qtDesigner로 화면 구성

CalUI = '_guiFiles/frame_test2.ui'


class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)
        self.setupUI()
        self.setFixedSize(800, 800)
        self.player1_idx = 0
        self.player2_idx = 0

    def setupUI(self):

        self.btn1.clicked.connect(self.dice_1)
        self.btn2.clicked.connect(self.dice_2)
        self.land1 = (
            (610, 470, 40, 40), (510, 470, 40, 40), (410, 470, 40, 40), (310, 470, 40, 40), (210, 470, 40, 40),
            (110, 470, 40, 40),
            (110, 370, 40, 40), (110, 270, 40, 40), (110, 170, 40, 40), (110, 70, 40, 40),
            (210, 70, 40, 40), (310, 70, 40, 40), (410, 70, 40, 40), (510, 70, 40, 40), (610, 70, 40, 40),
            (610, 170, 40, 40), (610, 270, 40, 40), (610, 370, 40, 40)
        )

        self.land2 = (
            (650, 510, 40, 40), (550, 510, 40, 40), (450, 510, 40, 40), (350, 510, 40, 40), (250, 510, 40, 40),
            (150, 510, 40, 40),
            (150, 410, 40, 40), (150, 310, 40, 40), (150, 210, 40, 40), (150, 110, 40, 40),
            (250, 110, 40, 40), (350, 110, 40, 40), (450, 110, 40, 40), (550, 110, 40, 40), (650, 110, 40, 40),
            (650, 210, 40, 40), (650, 310, 40, 40), (650, 410, 40, 40)
        )

    def dice_1(self):
        result = randint(1, 6)
        print(result)
        self.player1_idx += result
        if self.player1_idx > 17:
            self.player1_idx -= len(self.land1)
        self.player1.setGeometry(self.land1[self.player1_idx][0], self.land1[self.player1_idx][1],
                                 self.land1[self.player1_idx][2], self.land1[self.player1_idx][3])

    def dice_2(self):
        result = randint(1, 6)
        print(result)
        self.player2_idx += result

        if self.player2_idx > 17:
            self.player2_idx -= len(self.land2)
        self.player2.setGeometry(self.land2[self.player2_idx][0], self.land2[self.player2_idx][1],
                                 self.land2[self.player2_idx][2], self.land2[self.player2_idx][3])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    mainDialog.show()
    app.exec_()
