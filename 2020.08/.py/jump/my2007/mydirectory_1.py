import os


def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        line = f.readline()
        return line


with os.scandir('e:/realsong/pycharmprojects/jump/my_directory') as entries:
    for entry in entries:
        print(entry.name)
        text = read_data("my_directory\\%s" % entry.name)
        print(text)
