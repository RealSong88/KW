# Q1=====

# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# Q2=====================================


# def avg_number(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)
#
# print(avg_number(1, 2))
# print(avg_number(1,2,3,4,5))

# Q3===================

input1 = input("첫번째 숫자를 입력하시요:")
input2 = input("두번째 숫자를 입력하시요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." % total)