# num_one = 10
#
# if __name__ == "__main__" :
#     print(__name__)
#     print(id(num_one))
#     print(num_one)
#
#


# chr 함수 ord 함수 활용
# total = []
# string_object = "python"
# print(string_object)
# for i in string_object:
#     total.append(chr(ord(i)-32))
#
# print(i)
# print(total)

#
# print(chr(112)) # 'p'
# print(chr(112 - 32)) # 'P'
# print(ord('p')) # 112
# print(chr(ord('p') - 32)) # 'P'

# 함수의 매개변수 활용
# def progression(n, step=1):
#     x = 1
#     while x <= n:
#         print(x)
#         x += step
#
#
# progression(10)

# 258p
# def argsfunc(*args):
#     i = 0
#     for x in args:
#         i += 1
#     print("인수의 갯수 %d" % i)
#     print(args)
#
# argsfunc(1, 2, (3, 4, 5))
# argsfunc(1, [7, 55], "test", {'a': 1, 'b': 100})
#
#
# a = 1
# b = {3, 6, 9}
# c = {'x': 0, 'y': 99}
# argsfunc(a, b, c)

# 258p
# def dictsfunc(**dicts):
#     i = 0
#     for x in dicts.keys():
#         i += 1
#     print("인수의 개수: %d" % i)
#     print(dicts)
#
# # 키워드 인수 형태
# dictsfunc(a=1, b=2, c=3)
# # 사전 형태
# dictsfunc(**{'a': 1 , 'b': 2, 'c': 3})


# 튜플 형태 예제 262p
# def returnTuple(x, y, z):
#     return x, y, z
#
#
# # return은 한 개만 할 수 있다.
#
# x, y, z = returnTuple(1, 2, 3)
# print(x)
#
# # 여러개인 경우 tuple을 만들어 한 개를 반환!!
# print(returnTuple(1, 2, 3))
#
# a, b = (1, 2)
# print(a)


# 271p global 활용 myfunc 에서도 사용

# global_var = 77
#
# def myfunc():
#     global global_var
#     global_var += 1
#     print(global_var)
#
# myfunc()
# print(global_var)
# var = 77
#
# def func():
#     global var
#     var = 100
#     print(locals()) # {} global 변수로 지정했기때문에 지역변수가 없음
#
# func()
# print(var)
#
# def local_fun():
#     var = 100
#     print(locals()) # {'var': 100} 지역변수의 값이 있기때문에
#
# local_fun()

# 272p 중첩함수

# def outter():
#     def inner():
#         print("inner")
#
#     print(locals())  # outter() 지역 함수로 inner() 가 있다.
#     inner()
#
#
# outter()


# 273p 중첩의 중첩

# def outter():
#     a = 1
#
#     def inner1():
#         b = 2
#
#         def inner2():
#             c = 3
#             print(a, b, c)
#
#         inner2()
#
#     inner1()
#
#
# outter()
