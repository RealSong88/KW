# # 295p  제네레이터 .. for문은 반복을 끝날때까지하지만 제네레이터는 내가 원할 때 반복한다.

# a = [1, 2, 3, 4, 5]
# it = iter(a)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
#

# 296p
# 함수 내부에 yield 를 사용하면 제네레이터 함수가 된다.

# def my_gen():
#     n = 0
#     while n <= 10:
#         yield n
#         n += 1
#
# a = my_gen()
# type(a)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


