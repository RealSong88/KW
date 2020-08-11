import os


def dir_data(param_path):
    with os.scandir(param_path) as entries:
        txt = ""
        for entry in entries:
            # print(entry.name)
            with open(f'{param_path}/{entry.name}', 'r', encoding='utf8') as f:
                line = f.readline()
                # print(line)
                txt += f'{line},'
    return txt

def transform(data):
    data_list = data.split(",")
    new_list = []
    for i in range(int(len(data_list) / 2)):
        new_list.append([data_list[i * 2], int(data_list[i * 2 + 1])])
    return new_list


def mysum_list(ogr_list):
    sum_list = []
    for i in ogr_list:
        chk_dupl = False
        no_dupl = None
        for j in range(len(sum_list)):
            if sum_list[j][0] == i[0]:
                no_dupl = j
                chk_dupl = True
        if chk_dupl:
            sum_list[no_dupl][1] += i[1]
        else:
            sum_list.append(i)
    return sum_list

path = 'practice/200805'
data = dir_data(path)
print(data)

new_data = transform(data)
print(new_data)
print(mysum_list(new_data))