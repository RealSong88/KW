# data는 항상 초기화 되어야 한다.
# input "a,1,b,2,a,3"
data = []
data2 = []

sales = "a,1,b,2,a,3"
sales2 = "a,1,b,2,a,3"
sales3 = "a,1,b,2,a,3"
list = sales.split(",")
print(list)
# list = ['a',1,'b',2,'a',3]

length = len(list) # 6회
for i in range(length):
    # [[]]
    if i % 2 == 1:
        # print(i)
        data.append([list[i-1],int(list[i])])
print(data)
print("="*30)

# data = [['a',1],['b',2],['a',3]]
# data2 = [['a',1],['b',2]]
for j in data:
    is_dupl = False
    no_dupl = None
    for k in range(len(data2)):
        if data2[k][0] == j[0]:
            is_dupl = True
            no_dupl = k
    if is_dupl:
        data2[no_dupl][1] = j[1] + data2[no_dupl][1]
    else:
        data2.append(j)
print("="*30)
print(data2)
