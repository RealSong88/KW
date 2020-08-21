import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from mymodify.dice.user import User
from mymodify.menu import menu
from random import randint

# qtDesigner로 화면 구성
CalUI = 'e:/random_dice/mymodify/_guiFiles/frame.ui'


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)
        self.dice_pushButton.clicked.connect(self.dice)

    def dice(self):
        result = randint(1, 6)
        print(result)
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    mainDialog.show()
    app.exec_()
