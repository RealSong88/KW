num = input()
list = num.split(" ")
list_int = []
for i in list:
    list_int.append(int(i))
# print(list_int)
x = list_int[0]
y = list_int[1]
w = list_int[2]
h = list_int[3]


new_list = []
new_list.append(x)
new_list.append(y)
new_list.append(w - x)
new_list.append(h - y)
# print(new_list)

min = new_list[0]
for i in new_list:
    if i < min :
        min = i

print(min)


