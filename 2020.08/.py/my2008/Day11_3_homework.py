import random

# for i in range(1,101):



# x = random.randrange(1, 101)
# print(x)
# print()


# list_car.append(random.randrange(1,101))
# for i in range(5):
#     y = random.randrange(1, 101)
#     list_rfg = list_rfg + [y]
#
# print(list_rfg)
# new_list = []
# for i in range(len(list_rfg)):
#     chk_dupl = False
#     for j in range(len(new_list)):
#         if new_list[j] == list_rfg[i]:
#             chk_dupl = True
#     if chk_dupl :
#         pass
#     else:
#         new_list.append(list_rfg[i])
list = []
for i in range(1, 11):
    list.append(i)
new_list = []

x = random.randrange(1, 11)
new_list.append(list[x])

print(new_list)
list.pop(x)
print(list)

rfg_list = []

for i in list:
    y = random.randrange(1, len(list))
    rfg_list.append(i)
    list.pop(y)
    if len(rfg_list) == 5: break
# for i in range(len(list)):
#     y = random.randrange(1, len(list))
#     rfg_list = rfg_list + [y]


print(rfg_list)
print(list)
