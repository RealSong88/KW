def my_four_cal(sum, param):
    result = sum
    if "+" in param:
        result = sum + int(param[1:])
    elif "-" in param:
        result = sum - int(param[1:])
    elif "*" in param:
        result = sum * int(param[1:])
    elif "/" in param:
        result = sum / int(param[1:])
    return result

# print(my_four_cal(4, "/4"))
sum = None
while True:
    if not sum:
        sum = input("초기값 입력>")
    txt = input("입력...>")
    if txt == "q":
        break
    print("{}를 계산합니다. ".format(txt))
    sum = my_four_cal(int(sum), txt)
    print(sum)


    # else:
    #     sum = sum + input("계산식을 입력 > ")