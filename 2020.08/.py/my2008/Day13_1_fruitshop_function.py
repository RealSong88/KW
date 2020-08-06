import os



def read_dir(param_path):
    with os.scandir(param_path) as entries:
        for entry in entries:
            print(entry.name)
            items = read_data(param_path + "/%s" % entry.name)
            print(items)


def read_data(param_data):
    with open(param_data, "r", encoding="utf8") as f:
        line = f.readline()
        return line


data = "e:/realsong/pycharmprojects/jump/practice/200803"

read_dir(data)