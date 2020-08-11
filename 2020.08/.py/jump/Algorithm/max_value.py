from random import *
def max_cal(value_list):
    max = value_list[0]
    for i in value_list:
        if max < i :
            max = i
    return max

list = [17, 92, 18, 33, 58, 7, 33, 42]

max = list[0]
for i in list:
    if max < i:
        max = i
print(max)


print(max_cal(list))
min = list[0]
for i in list:
    if min > i:
        min = i
print(min)

max = list[0]
list_index = 0
for i in range(len(list)):
    if max < list[i] :
        list_index = i
        max = list[i]

print(list_index)



# alist = []
# for i in range(10):
#     j = randrange(1, 101)
#     alist = alist + [j]
#
# print(alist)
#
# print(max_cal(list))
# print(max_cal(alist))
