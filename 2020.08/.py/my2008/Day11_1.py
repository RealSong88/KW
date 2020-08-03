myfriends = {'a':'가,나','b':'다,라,마','c':'가,다,바'}
myfriends_list = []
myfriends_set = {}

#values 값을 ,으로 split 후에 myfriends_list 에 담는다.
for i in myfriends.values():
    myfriends_list = myfriends_list + (i.split(","))

print(myfriends_list)
myfriends_set = set(myfriends_list)
print(myfriends_set)
print("%d명이다. " % len(myfriends_set))

new_myf_list = sorted(set(myfriends_set))
print(new_myf_list)
# for i in myfriends.keys():
#     temp = myfriends[i].split(",")
#     for j in temp:
#
#     print(myfriends[i])
#     print(temp)

text = ""

for k in new_myf_list:
    # print(k)
    temp = ""
    # "가,나,다"
    for j in myfriends.keys():
        if k in myfriends[j]: # myfriends의 value 값에서 new_myf_list 의 k 값이 있다면 temp에 그 key값을 저장
            temp = temp+','+j
        # print(j)
    text = text + "{} = {}\n".format(k,temp)


print(text)

