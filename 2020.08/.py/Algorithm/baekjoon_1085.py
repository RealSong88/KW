
#
#
# comp = False
# while not comp:
#     num = input()
#     list = num.split(" ")
#     list_int = []
#     for i in list:
#         list_int.append(int(i))
#     if list_int[0] > 0 and list_int[0] < list_int[3]:



num = input()
list = num.split(" ")
list_int = []

for i in list:
    list_int.append(int(i))

print(list_int)
new_list = []
new_list.append(list_int[2] - list_int[0])
new_list.append(list_int[3] - list_int[1])
print(new_list)

min = new_list[0]
for i in new_list:
    if i < min :
        min = i

print(min)

# x = int(input())
# y = int(input())
# w = int(input())
# h = int(input())

# list1 = [x, y]
# list2 = [w, h]
# new_list = []
# new_list.append(list2[0] - list1[0])
# new_list.append(list2[1] - list1[1])
#
# print(new_list)
#
# min = new_list[0]

# for i in new_list:
#     if i < min :
#         min = i
#
# print(min)
#
