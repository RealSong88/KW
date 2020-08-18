import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# qtDesigner로 화면 구성
CalUI = '_uiFiles/frame.ui'


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)


        # self.dot_pushButton.clicked.connect(self.delete)
        # self.per_pushButton.clicked.connect(self.delete)

        # self.del_pushButton.clicked.connect(self.delete)
        # self.result_pushButton.clicked.connect(self.makeResult)
        # self.reset_pushButton.clicked.connect(self.reset)




app = QApplication(sys.argv)
mainDialog = MainDialog()
mainDialog.show()
app.exec_()
