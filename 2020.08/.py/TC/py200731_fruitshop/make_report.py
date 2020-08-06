# [['a',1],['b',1],['a',1],['c',1]]
# a,1\nb,1\nc,1형식의  csv파일
report_data = []

def check_dupl(item_list):
    # 중복여부, 중복인덱스
    for i in range(len(report_data)):
        if report_data[i][0] == item_list[0]:
            return True, i
    return False, None

def make_report(param_list):
    # [['a', 1], ['b', 1], ['a', 1], ['c', 1]]
    for i in param_list:
        # ['a', 1]
        is_dupl, idx_dupl  = check_dupl(i)
        if is_dupl:
            report_data[idx_dupl][1] = i[1] + report_data[idx_dupl][1]
        else:
            report_data.append(i)

make_report([['a',1],['b',1],['a',1],['c',1]])
make_report([['r',1],['b',5],['a',1],['c',1]])
print(report_data)