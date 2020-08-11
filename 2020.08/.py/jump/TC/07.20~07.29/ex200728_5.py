# input "a,1,b,2,a,3"
data = []
data2 = []

list = "a,1,b,2,a,3".split(",")
print(list)
# list = ['a',1,'b',2,'a',3]
length = len(list) # 6회
for i in range(length):
    # [[]]
    if i % 2 == 1:
        # print(i)
        data.append([list[i-1],int(list[i])])
print("="*30)
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
