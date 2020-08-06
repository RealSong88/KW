# str = "a,4,b,6,d,8,a,8,b,4,c,7,g,9,h,1,a,6,b,3,h,5"
# str_n = []
# index = 0
# for i in str:
#     if i == ",": # a 4 b 6 d 8
#         index = index + 1
#         print(index)


#
# str = "a,1,b,2,a,3"
# str_n = ""
# for i in str:
#     if i != ",":
#         str_n += i
# name = ""
# sums = ""
# i = 0
# while i < len(str_n) :
#     if i % 2 ==0:
#         name = name + str_n[i]
#     else :
#         sums = sums + str_n[i]
#     i += 1
#
# print(name)
# print(sums)
# i = 0

data = "ab,1,a,2,ab,3,"
index = 0
str = ""
old_str = ""
data_n = ""
data_v = ""

for i in data:
    str = str + i
    print(index, str)
    if i == ",":
        if index % 2 == 0:
            if data_n.find(str) == -1 :
              data_n = data_n + str
              index += 1
              old_str = str
              str = ""
        else:
            data_v = data_v + i
            index += 1
            str = ""
#
# print(data_n, data_v)