from PyQt5.QtCore import *

time = 0

def printTime(time) :
  time += 1
  print(time)

timerVar = QTimer()
timerVar.setInterval(1000)
timerVar.timeout.connect(printTime(time))
timerVar.start()