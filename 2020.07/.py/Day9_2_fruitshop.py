# source = "tomoto,1,grape,2,peach,3,grape,1,peach,3"


def list_s(param):  # 데이터를 리스트로 추출
    value_list = []
    temp = param.split(",")
    for i in range(int(len(temp) / 2)):
        value_list.append([temp[i * 2], int(temp[i * 2 + 1])])
    return value_list


def fruit_sum(param):  # 리스트를 가로 출력
    item = ""
    fr_num = ""
    for i in param:
        item = item + "{0:>10}".format(i[0])
        fr_num = fr_num + "{0:>10}".format(i[1])
    print("*" * len(item))
    print(item)
    print(fr_num)


def item_dupl(list, item): # 리스트안에 중복 여부 확인하는 함수
    for i in range(len(list)):
        if list[i][0] == item[0]:
            return True, i
    return False, None


# data = list_s(source)
# print(data)

# 새로운리스트에 중복이 없으면 데이터를 추가하고 중복이 있으면 수량을 더해주는 함수
def calc_total(list_o, list_n):
    for i in range(len(list_o)):
        item = list_o[i]
        is_dupl, no_dupl = item_dupl(list_n, item)
        if is_dupl:
            list_n[no_dupl][1] = item[1] + list_n[no_dupl][1]
        else:
            list_n.append(item)


s1 = "a,1,b,2,a,3"
s2 = "s,2,d,5,f,3,s,1"
s3 = "a,2,f,5,s,4,d,2"
sales = [s1, s2, s3]
data2 = []
# source들을 리스트화 시켜서 data2에 없는 데이터면 추가 중복되면 수량을 더해주게끔 작성
for sale in sales:
    list = list_s(sale)
    calc_total(list, data2)

print(data2)
