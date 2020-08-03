# multiline = "Life is too short\nYou need python"
# aList = []
# i = 0
# while i < len(multiline):
#     aList.append(multiline[i])
#     i += 1
# print(aList)
#
# print(multiline)

#=========================================

# a = "Life is too short, You need Python"
# count = 0
# for i in a:
#     if i == "o" :
#         print(i)
#         count +=1
# print("o는", count, "번 출력")
#
# print(a[8:14])


#============================== if문 for문 활용하여 문자열 인덱싱 및 슬라이싱

# for i in ["20010331Rainy", "331Rainy2001", "20Rainy331"]:
#     count = 0
#     for j in i:
#         if j == "a":
#             print(i[:count], i[count:])
#         count = count + 1

#=======연습문제 2장 Q3
pNumber = ["881120-1068234", "881120-1068sadf4", "881120-1068234", "881120-1068234"]
for i in pNumber:
    count = 0
    for j in i:
        if j == "-":
            print(i[:count], i[count+1:])
        count = count + 1

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second