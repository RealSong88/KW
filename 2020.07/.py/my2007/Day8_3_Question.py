#Q1

# def is_odd(n):
#     if n % 2 == 0:
#         return "짝수"
#     else:
#         return "홀수"
#
# print(is_odd(4))
# print(is_odd(3))

#Q2====================== 입력값을 받아서 리스트화 시키고 그것을 함수로 평균값 계산
#다시해보기 미완성
# def is_avg(r_list):
#     sum = 0
#     for i in r_list:
#         sum = sum + i
#     return sum / len(r_list)
# list = []
# value = int(input("값을 입력하시오 :"))
# list.append(value)
#
#
# print("평균값은 %d" % is_avg(list))

#Q3=====================

# input1 = int(input("첫번째 숫자를 입력하세요:"))
# input2 = int(input("두번째 숫자를 입력하세요:"))
#
# total = input1 + input2
## or
## total = int(input1) + int(input2)
# print("두 수의 합은 %s 입니다" % total)

#Q4==================

# 3번 , 는 문자열사이에 공백이 생긴다.

#Q5===============

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
# f2 = open("test.txt", 'r')
# line = f2.readline()
# print(line)
# f2.close()

#Q6===================

# user_input = input("내용을 입력하세요: ")
# f = open("test2.txt", 'a')
# f.write(user_input)
# f.write("\n")
# f.close()

#Q7======================
#
# f = open("test.txt", 'r')
# lines = f.read()
# f.close()
# lines = lines.replace("java", "python")

# f1 = open("test.txt", 'w')
# f1.write(lines)
# f1.close()