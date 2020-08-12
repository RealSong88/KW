import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

CalUI = '_uiFiles/calculator.ui'


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.numClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.numClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.numClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.numClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.numClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.numClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.numClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.numClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.numClicked(state, button))
        self.num_pushButton_10.clicked.connect(lambda state, button = self.num_pushButton_10 : self.numClicked(state, button))

        self.sign_pushButton_1.clicked.connect(lambda state, button = self.sign_pushButton_1: self.numClicked(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button = self.sign_pushButton_2: self.numClicked(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button = self.sign_pushButton_3: self.numClicked(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button = self.sign_pushButton_4: self.numClicked(state, button))

        self.result_pushButton.clicked.connect(self.makeResult)
    def numClicked(self, state, button):
        exist_line_text = self.q_lineEdit_1.text()
        now_num_text = button.text()

        self.q_lineEdit_1.setText(exist_line_text + now_num_text)

    def makeResult(self):
        result = eval(self.q_lineEdit_1.text())
        self.q_lineEdit_2.setText(str(result))



app = QApplication(sys.argv)
mainDialog = MainDialog()
mainDialog.show()
app.exec_()
