import sys
from PyQt5.QtWidgets import *
from mymodify.GUI.play import MainDialog


# 두번째 윈도우창 인원 수, 생명 설정창.

class SettingBase(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.person = None
        self.life = None

    def setupUI(self):
        self.setFixedSize(400, 300)
        self.setGeometry(1110, 500, 400, 300)
        self.setWindowTitle("설정")

        label1 = QLabel("인원 수: ")
        label2 = QLabel("라이프 : ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1 = QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.person = self.lineEdit1.text()
        self.life = self.lineEdit2.text()
        print(self.person)
        print(self.life)

        # play.py의 클래스 3번째 윈도우
        dlg = MainDialog()
        dlg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    set = SettingBase()
    set.show()
    app.exec_()
