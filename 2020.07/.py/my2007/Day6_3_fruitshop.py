data = "apple,1,banana,2,apple,4,kiwi,4"
index = 0
listD = data.split(",")
newlist = []
name = ""
value = ""
print(listD)

for i in range(len(listD)):
    templist = []
    if i % 2 == 1:
        templist.append(listD[i-1])
        templist.append(int(listD[i]))
        newlist.append(templist)


print(len(newlist))
print(newlist)

newlist2 = []

for i in range(len(newlist)): #0 1 2 3
    is_dupl = False
    for j in range(len(newlist2)):
        if newlist2[j][0] == newlist[i][0]:
            is_dupl = True
            newlist2[j][1] += newlist[i][1]
    if is_dupl:
        pass
    else:
        newlist2.append(newlist[i])
dataN = ""
dataV = ""
for i in range(len(newlist2)):
    dataN += "{0:>10}".format(newlist2[i][0])
    dataV += "{0:>10}".format(newlist2[i][1])

    #print("%s의 갯수는 %d 이다 " % (newlist2[i][0], newlist2[i][1]))
print("="*30)
print(dataN)
print(dataV)



