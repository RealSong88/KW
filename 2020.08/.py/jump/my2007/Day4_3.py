from datetime import datetime

now = datetime.now().strftime('%m-%d')

getNum = []
for i in now :
    getNum.append(i)

num0 = ["\n{0:^5}".format("***"), "\n*   *", "\n*   *", "\n*   *", "\n*   *", "\n*   *", "\n{0:^5}".format("***")]
num1 = ["\n{0:>5}".format("*"), "\n{0:>5}".format("*"), "\n{0:>5}".format("*"), "\n{0:>5}".format("*"), "\n{0:>5}".format("*")]
num2 = ["\n{0:^5}".format("***"), "\n*   *", "\n{0:>4}".format("*"), "\n{0:>3}".format("*"), "\n*   ", "\n*   ", ("\n*****" )]
num3 = ["\n{0:^5}".format("***"),("\n*   *"),"\n{0:>5}".format("*"),"\n{0:^5}".format("***"),"\n{0:>5}".format("*"),"\n*   *", "\n{0:^5}".format("***")]
num7 = ["\n*" * 5, "\n*   *", "\n{0:>5}".format("*"), "\n{0:>5}".format("*"), "\n{0:>5}".format("*"), "\n{0:>5}".format("*")]
num_ = ["\n","\n","\n","\n*****","\n","\n",""]
f1 = open("data0.txt", "w")

print(getNum)

for i in getNum:
    if i == "0" :
        for j in num0:
         f1.write(j)
         print(j)

    elif i == "1":
        for j in num1:
            f1.write(j)
            print(j)
    elif i == "2":
        for j in num2:
            f1.write(j)
    elif i == "3":
        for j in num3:
            f1.write(j)
            print(j)
    elif i == "7":
        for j in num7:
            f1.write(j)
            print(j)
    elif i == "-":
        for j in num_:
            f1.write(j)
            print(j)

# for i in getNum:
#     for j in range(0,11):
#         if i == "0":
#             f1.write(num0)
#             print(num0)
#         elif i == "1":
#             print(num1)
#             f1.write(num1)
#         elif i == "2":
#             print(num2)
#             f1.write(num2)
#         elif i == "3":
#             print(num3)
#             f1.write(num3)
#         elif i == "7":
#             print(num7)
#             f1.write(num7)
#         elif i == "-":
#             print(num_)
#             f1.write(num_)


# for i in num_ :
#     data = i
#     f1.write(data)
#     print(data)
#
# f1.close()


# f = open("today.txt", 'w')
#
#
#
# f.close()







