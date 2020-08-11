source = "banana,7,melon,3,banana,2"
data = []
data2 = []

# source 를 넣어서 리스트로 데이타를 추출하는 함수
def transform_list(param):
    temp = source.split(",")
    for i in range(int(len(temp) / 2)):
        data.append([temp[i * 2], int(temp[i * 2 + 1])])
    return data


data = transform_list(source)

print(data)

for i in data:
    is_dupl = False
    no_dupl = None
    for j in range(len(data2)):
        if i[0] == data2[j][0]:
            is_dupl = True
            no_dupl = j
    if is_dupl:
        data2[no_dupl][1] = data2[no_dupl][1] + i[1]
    else:
        data2.append(i)

print(data2)
