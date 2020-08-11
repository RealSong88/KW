#새로운 data2 객체를 만든 version
# source = "a,1,b,2,c,3,a,4,d,5,f,6,c,7"
source = "a,1,b,2,a,2"
# data = [['a',1],['b',1],['c', 1],['a',1]['d',1],['f',1],['c',1]]
temp = source.split(",")
data = []


for i in range(len(temp)):
    if i % 2 == 1:
        data.append([temp[i-1], int(temp[i])])

print(data)
print("="*50)

data2 = []
#
#i 는 ['a', 1]과 같은 리스트
for i in range(len(data)):
    is_dupl = False
    no_dupl = None
    # 중복여부확인
    # 중복되는 인덱스 번호를 알아야 한다.
    for j in range(len(data2)):
        if data2[j][0] == data[i][0]:
            is_dupl = True
            no_dupl = j
    if is_dupl:
        sum = data[i][1] + data2[no_dupl][1]
        #data2[no_dupl][1] = sum
        data2[no_dupl] = [data2[no_dupl][0], sum]

    else:
        # data2.append(data[i])
        data2 = data2 + [[data[i][0], data[i][1]]]

print(data2)
print(data)

# #i 는 ['a', 1]과 같은 리스트
# for i in range(len(data)):
#     is_dupl = False
#     for j in range(len(data2)):
#         if data2[j][0] == data[i][0] :
#             is_dupl = True
#             data2[j][1] += data[i][1]
#     if is_dupl :
#         print("중복입니다.")
#         pass
#     else:
#         data2.append(data[i])
#
# print(data2)


# for i in range(len(temp)) :
#     sub_data = []
#     if i % 2 == 0:
#         sub_data.append(temp[i])
#         sub_data.append(int(temp[i+1]))
#         data.append(sub_data)
# print(data)
