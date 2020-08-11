data = "apple,1,banana,2,apple,4,kiwi,4"
index = 0
listD = []
listD = data.split(",")
name_set = []
name = ""
value = ""
print(listD)
print(len(listD))

for i in listD:
    if index % 2 == 0:
        if i not in name_set:
            name_set.append(i)

            value = "{0}{1:10}".format(value, "0") #"{0:10}".format(listD[index])
    index += 1

print(name)
print(name_set)
print(value)


# name = ""
# value = ""

# ['apple', '1', 'banana', '2', 'apple', '4', 'kiwi', '4']
# name = apple     banana    apple     kiwi
# value = 1         2         4         4

# for i in listD:
#     if index % 2 == 1:
#         print("%s에 %s를 더한다." % (listD[index-1], listD[index]))
#     index += 1

