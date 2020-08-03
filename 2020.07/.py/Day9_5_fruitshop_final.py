import os


# 소스를 2차원리스트화 시키는 함수
def trans_list(source):
    data = []
    temp = source.split(",")
    for i in range(int(len(temp) / 2)):
        data.append([temp[i * 2], int(temp[i * 2 + 1])])
    return data


# 중복 유무를 구별하는 함수
def mydupl(new_data, item):
    for i in range(len(new_data)):
        if new_data[i][0] == item[0]:
            return True, i
    return False, None  # 들여쓰기의 중요성 for 문 안으로 들어가면 리턴값이 아예 없음


# sum_list 란 매개변수에 값이없으면 추가하고 중복되면 더하는 함수
def my_sum_list(ogr_list, sum_list):
    for i in range(len(ogr_list)):
        item = ogr_list[i]
        is_dupl, no_dupl = mydupl(sum_list, item)
        if is_dupl:
            sum_list[no_dupl][1] = sum_list[no_dupl][1] + item[1]
        else:
            sum_list.append(item)


    return sum_list


# 파일의 데이터를 읽어와서 line에 저장하고 반환하는 함수
def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        line = f.readline()
        return line


def fruit_print(param):  # 리스트를 가로 출력
    item = ""
    fr_num = ""
    for i in param:
        item = item + "{0:>10}".format(i[0])
        fr_num = fr_num + "{0:>10}".format(i[1])
    print("읽어온 데이터의 합을 구합니다..")
    print("*" * len(item))
    print(item)
    print(fr_num)


final_sum = []
with os.scandir('practice') as lists:  # 특정경로의 파일 목록을 불러온다
    for list in lists:
        sale = read_data("practice\\%s" % list.name)  # 파일의 데이터를 추출한다.
        print("%s 를 읽고있습니다..." % list.name)
        ogr_list = trans_list(sale)
        fruit_print(ogr_list)
        final_sum = my_sum_list(ogr_list, final_sum)
        print()


fruit_print(final_sum)

# with open("sum_list.txt", "w", encoding='utf8') as f:
#     for i in sum_list:
#         # print("%s, %s\n" % (i[0], i[1]))
#         f.write("%s, %s\n" % (i[0], i[1]))
