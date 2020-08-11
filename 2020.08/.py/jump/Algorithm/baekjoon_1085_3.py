x = 0
y = 0
w = 0
h = 0


input_list = []
input_split = ""

while True:
    input_number = input("숫자를 입력하시오")

    input_split = input_number.split(" ")

    for i in range(len(input_split)):
        input_split[i] = int(input_split[i])

    # 0 - x, 1 - y, 2 - w, 3 - h

    if input_split[2] >= 1000:
        print("w가 1000보다 큽니다. 다시 입력하세요")
        continue
    elif input_split[3] >= 1000:
        print("h가 1000보다 큽니다. 다시 입력하세요")
        continue
    elif not (input_split[0] >= 1 and (input_split[2]-1) >= input_split[0]):
        print("x가 1보다 작거나, w-1보다 큽니다")
        continue
    elif not (input_split[1] >= 1 and (input_split[3]-1) >= input_split[1]):
        print("y가 1보다 작거나, h-1보다 큽니다")
        continue
    else: break


# 0 - x, 1 - y, 2 - w, 3 - h
high_y =  input_split[3] - input_split[1]
#h-y
low_y = input_split[1] - 0
#y-0
high_x = input_split[2] - input_split[0]
#w-x
low_x = input_split[1] - 0
#y-0

number = []
number.append(high_y)
number.append(low_y)
number.append(high_x)
number.append(low_x)
number.sort()

min = number[0]

print(min)




