source = "a,2,b,1,c,1,a,1,d,1,f,1,c,1"
# data = [['a',1],['b',1],['c',1],['a',1],['d',1],['f',1],['c',1]]
temp = source.split(',')
# temp = ['a','1' ... 'c','1']
data = []

def feat1():
    # 인덱스 번호를 i에 담는다
    for i in range(len(temp)):
        if i%2 == 1:
            print(i, [temp[i-1], int(temp[i])])
            data.append([temp[i-1], int(temp[i])])

    print(data)
    print("="*30)

data2 = []
# j는 ['a',1]와 같은 리스트
for j in range(len(data)):
    # 중복여부를 확인하고
    is_dupl = False
    no_dupl = None
    # 중복되는 인덱스 번호를 알아야 한다.
    for k in range(len(data2)):
        if data2[k][0] == data[j][0]:
        #     print(data2[k][0], data[j][0])
            is_dupl = True
            no_dupl = k
    if is_dupl:
        print("중복입니다.")
        sum = data[j][1] + data2[no_dupl][1]
        data2[no_dupl][1] = sum
    else:
        data2.append(data[j])
    print(is_dupl,data2)

# print(data2)