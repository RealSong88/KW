# i = 0
# f = open("e:\\gugudan.txt ", "w")
# while i < 9 :
#     i += 1
#     result = i * 2
#     print("2 X %d = %d" % (i, result))
#     data = "2 X %d = %d\n" % (i, result)
#     f.write(data)
#
# f.close()
#
# f = open("E:\\RealSong\\Documents\\gugudan.txt", "w")
# for i in range(2, 10):
#     data = "=========%d단===========\n" %i
#     f.write(data)
#     for j in range(1, 10):
#         result = i * j
#         print("%d X %d = %2d" %(i, j, result))
#         data = "%d X %d = %2d\n" %(i, j, result)
#         f.write(data)
# f.close()


for i in range(1, 10):
    for j in range(2, 5):
        result = i * j
        print("%d X %d = %2d" %(j, i, result) , end = "\t")

    print()
print()

for i in range(1, 10):
    for j in range(5, 8):
        result = i * j
        print("%d X %d = %2d" % (j, i, result), end="\t")

    print()

print()
for i in range(1, 10):
    for j in range(8, 10):
        result = i * j
        print("%d X %d = %2d" % (j, i, result), end="\t")

    print()


