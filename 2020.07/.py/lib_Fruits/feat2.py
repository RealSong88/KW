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
            print("중복입니다.")
            sum = old_data[i][1] + new_data[no_dupl][1]
            new_data[no_dupl][1] = sum
        else:
            new_data.append(old_data[i])

    return new_data

def my_dupl(old_data, new_data):
    for i in range(len(old_data)):
        is_dupl = False
        for j in range(len(new_data)):
            if new_data[j][0] == old_data[i][0]:
                new_data[j][1] += old_data[i][1]
                is_dupl = True
        if is_dupl :
            pass
        else :
            new_data.append(old_data[i])
    return new_data