a = [5,7,4,9,6,3,15]

b = [5,7,4,9,6,3,15,21]


def median_cal(param):
    param.sort()
    print(param)
    if int(len(param)) % 2 == 1: # 리스트 길이가 홀수 일 때
        mda_index = int(len(param)/2)
        return param[mda_index]
    else: # 짝수 일 때
        mda_index1 = int(len(param)/2) - 1
        mda_index2 = int(len(param)/2)
        return (param[mda_index1] + param[mda_index2]) / 2

print(median_cal(a))
print(median_cal(b))