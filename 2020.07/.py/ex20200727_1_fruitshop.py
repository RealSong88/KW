source = "a,1,b,2,c,3,a,1,d,2,c,3"
temp = source.split(",")
data=[]
for i in range(len(temp)):
    sub_list = []
    if i % 2 == 1:
        sub_list.append(temp[i-1])
        sub_list.append(int(temp[i]))
        data.append(sub_list)

print(data)
data2 = []
for i in range(len(data)):
    is_dupl = False
    no_dupl = None
    for j in range(len(data2)):
        if data2[j][0] == data[i][0]:
            is_dupl = True
            no_dupl = j
    if is_dupl:
        sum = data[i][1] + data2[no_dupl][1]
        data2[no_dupl][1] = sum

    else :
        data2.append(data[i])

print(data2)