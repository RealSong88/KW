source = "1,2,3,5,7,1,34,4"
i = "5"

# my version
# def mydupl(source, num):
#     list_s = source.split(",")
#     sub = ""
#     result = False
#     for i in list_s:
#         if i == num :
#             sub = sub + i
#     if len(sub) > 0 :
#         result = True
#     return result
#
# print(mydupl(source, i))


# teacher version
def find_com(list, value):
    result = False
    for i in list:
        if i == value:
            result = True
    return result

def tdupl(source, num):
    list_s = source.split(",")
    print(list_s)
    print(num)
    result = False
    if find_com(list_s, num):
        result = True
    return result

print(tdupl(source, i))