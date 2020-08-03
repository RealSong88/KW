def num0():
    print("{0:^5}".format("***"))
    print("*   *")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*   *")
    print("{0:^5}".format("***"))
def num1():
    print("{0:>5}".format("*"))
    print("{0:>5}".format("*"))
    print("{0:>5}".format("*"))
    print("{0:>5}".format("*"))
    print("{0:>5}".format("*"))
def num2():
    print("{0:^5}".format("***"))
    print("*   *")
    print("{0:>4}".format("*"))
    print("{0:>3}".format("*"))
    print("*   ")
    print("*   ")
    print("*" * 5)
def num3():
    print("{0:^5}".format("***"))
    print("*   *")
    print("{0:>5}".format("*"))
    print("{0:^5}".format("***"))
    print("{0:>5}".format("*"))
    print("*   *")
    print("{0:^5}".format("***"))
def num7():
    print("*" * 5)
    print("*   *")
    print("{0:>5}".format("*"))
    print("{0:>5}".format("*"))
    print("{0:>5}".format("*"))
    print("{0:>5}".format("*"))
def num_():
    print()
    print()
    print()
    print("*" * 5)
    print()
    print()
    print()

from datetime import datetime

now = datetime.now().strftime('%m-%d')

getNum = []
for i in now :
    getNum.append(i)


f = open("today.txt", 'w')

for i in getNum :
    if i == "0" :
        num0()
    elif i == "1":
        num1()
    elif i == "2" :
        num2()
    elif i == "3":
        num3()
    elif i == "4" :
        num4()
    elif i == "5" :
        num5()
    elif i == "6" :
        num6()
    elif i == "7" :
        num7()
    elif i == "8" :
        num8()
    elif i == "9" :
        num9()
    elif i == "-":
        num_()


f.close()







