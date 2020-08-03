
#문자열에서 리스트로 추출해서 i값과 비교해 참, 거짓을 반환하는 함수
source = "1,2,3,4"
#temp = source.split(",")
i = '2'
# ================= 내가 작성
def dupl(a, b) :
    s_list = source.split(",")
    result = False
    print(s_list)
    print(b)
    sub = ""
    for i in s_list:
        if i == b:
            sub = sub + i # 중복이 되면 sub에 a의 값을 더함
    if len(sub) > 0: # 중복된 값이 있으면 길이는 0 이상이기 때문에 result = True
        result = True
    return result

print(dupl(source, i))

#
# def findItem(pl, pi):
#     temp = False
#     for i in pl:
#         if i == pi:
#             temp = True
#     return temp
#
#
# #source에 두자리 이상의 수 입력시 find함수론 에러가 날 수 있음
# def chk_dupl(ps, pi):
#     temp = False
#     list_s = ps.split(",")
#     if findItem(list_s, pi):
#         temp = True
#     # if ps.find(pi) > -1:
#     #     temp = True
#     # else:
#     #     temp = False
#     return temp
#
# print(chk_dupl(source, i))