#문자열을 받아 2차원 리스트로 추출

def kvstr_to_list(param):
    result = []
    list = param.split(",")
    for i in range(int(len(list)/2)):
        tmp_list = [list[i*2], list[i*2+1]]
        result.append(tmp_list)
    return result

data = kvstr_to_list("a,1,b,1,c,1,a,4")
print(data)