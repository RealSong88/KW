
#
# f1 = open("mygugudan.txt", "w")
# for i in [2, 5, 8]:
#     for j in [1,2,3,4,5,6,7,8,9]:
#         if i == 8:
#             data = "%d X %d = %2d   %d X %d = %2d\n" %(i, j, (i * j), (i+1), j, ((i+1)*j))
#             print(data)
#             f1.write(data)
#         else:
#             data = "%d X %d = %2d   %d X %d = %2d   %d X %d = %2d\n" %(i, j, (i * j), (i+1), j, ((i+1)*j), (i+2), j, ((i+2)*j))
#             print(data)
#             f1.write(data)
#     print()



f = open("regugudan.txt", "w")

for i in [2, 4, 6, 8] :
    print()
    f.write("\n")
    for j in [1,2,3,4,5,6,7,8,9]:
        data = "%d * %d = %d \t %d * %d  = %d\n" % (i, j, (i*j), (i+1), j, (i+1)*j)
        print(data)
        f.write(data)




























