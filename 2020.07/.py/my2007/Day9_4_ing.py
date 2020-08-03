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


# 추출한 품목의 합을 구해 리스트로 저장하는 함수
def my_sum_list(ogr_list, sum_list):
    for i in range(len(ogr_list)):
        item = ogr_list[i]
        is_dupl, no_dupl = mydupl(sum_list, item)
        if is_dupl:
            sum_list[no_dupl][1] = sum_list[no_dupl][1] + item[1]
        else:
            sum_list.append(item)


# ====================================== 밑부분은 다시 해보자
# 파일을 읽어서 line1에 저장하고 return 하는 함수
def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        return line1


sales = []
data2 = []
# 'practice' 경로에 파일들을 리스트화 시키고 그 리스트에서 read_data로 데이타를 읽어서 sales 리스트에 append한다.
with os.scandir('practice') as lists:
    for list in lists:
        print(list.name)
        list = read_data("practice\\%s" % list.name)
        sales.append(list)

# append 된 리스트들을 2차원배열로 값을 추출한후에 중복되면 값을 합치고 없으면 data2에 데이타를 추가한ㄷㅏ.
for sale in sales:
    list = trans_list(sale)
    my_sum_list(list, data2)

print(data2)

# for sale in sales :
#     list = trans_list(sale)   #변수의 중요성
#     my_sum_list(list, data2)
# print(data2)
# # list = trans_list(source)
# # print(list)
# #
# # my_sum_list(list, data2)
# # print(data2)
