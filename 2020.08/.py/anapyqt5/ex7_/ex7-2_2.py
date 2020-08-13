import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        self.btn1 = QPushButton('big', self)
        self.btn1.setText('setTExt')

        btn2 = QPushButton('small', self)
        btn2.setCheckable(True)
        # btn2.toggle()

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

        # self.btn1.setIcon(QIcon('save.png'))
        self.btn1.clicked.connect(self.myclicked)
        self.btn1.pressed.connect(self.myPressed)
        self.btn1.released.connect(self.myReleased)

        btn2.released.connect(self.myReleased)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def resizeBig(self):
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)

    def myPressed(self):
        print("pressed")

    def myReleased(self):
        print("released")
    def myclicked(self):
            self.btn1.setIcon(QIcon('save.png'))

    def myToggled(self):
        print("toggle toggle~")
        self.btn1.setIcon(QIcon('save.png'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
