source = "a,1,b,2,c,3,a,4,d,5,f,6,c,7"
# data = [['a',1],['b',1],['c', 1],['a',1]['d',1],['f',1],['c',1]]
temp = source.split(",")
data = []


for i in range(len(temp)):
    if i % 2 == 1:
        data.append([temp[i-1], int(temp[i])])

print(data)
print("="*50)

data2 = []

#i 는 ['a', 1]과 같은 리스트


def chk_dupl(old_data, new_data):
    for i in range(len(old_data)):
        is_dupl = False
        no_dupl = None
        # 중복여부확인
        # 중복되는 인덱스 번호를 알아야 한다.
        for j in range(len(new_data)):
            if new_data[j][0] == old_data[i][0]:
                is_dupl = True
                no_dupl = j
        if is_dupl:
            sum = old_data[i][1] + new_data[no_dupl][1]
            new_data[no_dupl][1] = sum
            new_data[no_dupl] = [new_data[no_dupl][0], sum]
        else:
            new_data.append(old_data[i])

    return new_data

print(chk_dupl(data, data2))
