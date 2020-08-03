from lib_Fruits import feat1, feat2
# source = "a,1,b,2,c,3,a,4,d,5,f,6,c,7"
# data = [['a',1],['b',1],['c', 1],['a',1]['d',1],['f',1],['c',1]]
data2 = []

sales = "a,1,b,2,a,3"
sales2 = "a,1,b,2,a,3"
sales3 = "a,1,b,2,a,3"
data = feat1.feat1(sales)
# print(data)
data2 = feat2.my_dupl(data, data2)

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


print(data2 + data2)
print(data2)

