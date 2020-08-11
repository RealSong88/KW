from PyQt5.QtCore import QDate, Qt, QTime
from PyQt5.QtCore import QDateTime
# 날짜 출력하기
# now = QDate.currentDate()
# print(now.toString())
# print()
# print(now.toString('yy.M.d'))
# print(now.toString('yyyy.MM.dd'))
# print(now.toString("yyyy.MMM.ddd"))
# print(now.toString(Qt.ISODate))
# print(now.toString(Qt.DefaultLocaleLongDate))
# print(now.toString('yyyyMMdd'))

# 시간 출력하기
# time = QTime.currentTime()
# print(time.toString('h:m:s'))
# print(time.toString('hh:mm:ss'))
# print(time.toString('hh.mm.ss:zzz'))
# print(time.toString(Qt.DefaultLocaleLongDate))
# print(time.toString(Qt.DefaultLocaleShortDate))

# 날짜와 시간 표시하기

datetime = QDateTime.currentDateTime()
print(datetime.toString('yy.M.d Hhh:mm:ss'))
print(datetime.toString('yyyy.MM.dd, hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))