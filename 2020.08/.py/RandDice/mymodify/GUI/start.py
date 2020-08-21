import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


CalUI = 'e:/random_dice/mymodify/_guiFiles/start.ui'
from mymodify.GUI import play


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(CalUI, self)
        self.start_pushButton.clicked.connect(self.clicked_option)
        self.quit_pushButton.clicked.connect(self.close)

    def clicked_option(self):
        dlg = play.MainDialog(self)
        dlg.exec_()

    # def main_game(self):
    #     app1 = QApplication(sys.argv)
    #     mainDialog = form1.MainDialog()
    #     mainDialog.show()
    #     app1.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = MyApp()
    start.show()
    app.exec_()
