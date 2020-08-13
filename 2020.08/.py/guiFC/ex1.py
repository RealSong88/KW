import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Quit", self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage('Ready')

        self.setWindowTitle("My App")
        self.setGeometry(860, 200, 400, 300)
        self.show()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())