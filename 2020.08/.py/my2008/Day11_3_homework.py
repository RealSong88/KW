import random

list = []
for i in range(1, 11):
    list.append(i)

# 열개의 값중에 하나를 빼고 새로운 리스트에 그 값을 담는다.
# new_list = []
# x = random.randrange(1, len(list))
# new_list.append(list[x])
#
# print(new_list)
# list.pop(x)
# print(list)
print(list)

ranking = []
# 6번 반복해서 6개의 random y값을 만들고 ranking 리스트에 추가, 원래 list에서 중복값 제거
for i in range(6):
    y = random.randrange(1, len(list))
    ranking.append(list[y])
    list.pop(y)

for i in range(len(ranking)):
    if i == 0 :
        print("자동차 %2s번 당첨" % ranking[i])
    else:
        print("냉장고 %2s번 당첨" % ranking[i])
print(list)

#
# for i in list:
#     y = random.randrange(1, len(list))
#     rfg_list.append(i)
#     list.pop(y)
#     if len(rfg_list) == 5: break
# # for i in range(len(list)):
# #     y = random.randrange(1, len(list))
# #     rfg_list = rfg_list + [y]
#
#
# print(rfg_list)
# print(list)
