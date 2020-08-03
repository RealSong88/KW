data = "apple,1,banana,2,apple,4,kiwi,4"

index = 0
name = ""
sums = ""
str = ""
old_str = ""
for i in data:
    str = str + i
    # print(i,index, str)
    if i == ",":
        if index % 2 == 0:
            # 이미 apple이 있으면 넣지 않는다.
            if name.find(str) == -1:
                name = name + str
                sums = sums + "0,"
                old_str = str
        else: # index가 홀수일때 (=숫자값)
            print(name)
            print(sums)
            print(old_str, "에 값을 더한다.",str)
        index = index + 1
        str = ""

print(name, sums)