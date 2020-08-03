data = "apple,1,banana,2,apple,4,kiwi,4"
index = 0
listD = []
listD = data.split(",")
name = ""
value = ""
print(listD)
print(len(listD))

for i in listD:
    if index % 2 == 0 :
        name += "{0:10}".format(listD[index])
    else :
        value += "{0:10}".format(listD[index])
    index += 1

print(name)
print(value)

print("*"*50)
index = 0
name = ""
value = ""
sum = 0
name_index = 0
list_com = []

for i in listD:
    if index % 2 == 0:
        if i not in list_com:
            list_com.append(i)
    else :
        pass
    index += 1
print(list_com)
print(name)


# index = 0
# list_a = ['a', 'b', 'c','a','f','c']
# list_b = []
# for i in list_a :
#     if i not in list_b:
#      list_b.append(i)
#
# print(list_b)
#
# list_c = []
# for i in list_a:
#     if i not in list_c:
#         list_c.append(i)
# print(list_c)