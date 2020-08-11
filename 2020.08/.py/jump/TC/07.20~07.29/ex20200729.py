#tVersion
# a=[1,2,3] b=1 1일때 실행을 안하고 2, 3일때만 저장

# a = [1,2,3]
# b = 1
# if b in a:
#     print("T")
# else:
#     print("F")
#
# if b not in a:
#     print("F")
# else:
#     print("T")

#===========
#
# gas = int(input("얼마나 넣을까? "))
# while True:
#     print("엔진작동!!")
#     gas = gas -1
#     if gas < 1:
#         gas = int(input("더넣을까요?"))
#         if gas == 0 :
#             break
#         else:
#             pass

#=====================
# a = [1,2,3,4]
# b = []
# for num in a:
#     n = num * 3
#     b.append(n)
#     print(b)

#=============================

f = open("new_01.txt", "w")
f.write("나다용요용요로요롱롱")
f.close()

f = open("new_01.txt", "r")
line = f.readline()
print(line)
f.close()