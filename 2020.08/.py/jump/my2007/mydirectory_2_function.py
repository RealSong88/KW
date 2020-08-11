import os


def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        line = f.readline()
        return line


folder = 'e:/realsong/pycharmprojects/jump/my_directory'


# 특정경로를 주면 그 안에 폴더의 파일이름을 불러오는 함수
def dir_list(param_str):
    with os.scandir(param_str) as entries:
        lists = []
        for entry in entries:
            lists.append(entry.name)
            # lists = entry.name
        # print(lists)
        return lists
        # text = read_data("param_str\\%s" % entry.name)
        # print(text)


dir_list(folder)
