import os

def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        print(line1)


with os.scandir('practice') as lists:
    for list in lists:
        print(list.name)
        read_data("practice\\%s" % list.name)

print(type(lists))