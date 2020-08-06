source = "a,1,b,2,c,3,a,4"

temp = source.split(",")

data=[]
data2=[]

for i in range(len(temp)):
    if i % 2 == 0:
        data.append([temp[i], int(temp[i+1])])
print(data)

# for i in range(len(data)):
#     is_dupl = False
#     for j in range(len(data2)):
#         if data2[j][0] == data[i][0]:
#             data2[j][1] += data[i][1]
#             is_dupl = True
#     if is_dupl:
#         pass
#     else:
#         data2.append(data[i])

for i in data:
    is_dupl = False
    no_dupl = None
    for j in range(len(data2)):
        if data2[j][0] == i[0]:
            no_dupl = j
            is_dupl = True
    if is_dupl :
        data2[no_dupl][1] += i[1]
        pass
    else:
        data2.append(i)

print(data2)