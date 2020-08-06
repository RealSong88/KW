# sum = None
# def my_four_cal(sum, param):
#     result = sum
#     if "+" in param:
#         result = sum + int(param[1:])
#     elif "-" in param:
#         result = sum - int(param[1:])
#     elif "*" in param:
#         result = sum * int(param[1:])
#     elif "/" in param:
#         result = sum / int(param[1:])
#     return result
#
# # print(my_four_cal(4, "/4"))
#
# while True:
#     if not sum:
#         sum = input("초기값 입력>")
#     txt = input("입력...>")
#     if txt == "q":
#         break
#     print("{}를 계산합니다. ".format(txt))
#     sum = my_four_cal(int(sum), txt)
#     print(sum)
#

source = "+11*2"
data = []
sign = []
num = []
for i in source:
    data.append(i)
print(data)

for i in data :
    if i == "+":
        sign.append(i)
    elif  i == "-":
        sign.append(i)
    elif  i == "*":
        sign.append(i)
    elif i == "/":
        sign.append(i)
    else:
        num.append(i)


print(sign)
print(num)