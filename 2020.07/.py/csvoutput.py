source = [['a',3],['b',6],['c',2],['r',1]]
print(source)

with open("csvoutput.csv", "w", encoding='utf8') as f:
    for i in source:
        # print("%s, %s\n" % (i[0], i[1]))
        f.write("%s, %s\n" % (i[0], i[1]))
