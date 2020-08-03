# money = 0
# taxi = 3500
# bus = 1600
# card = False
#
# if money >= taxi :
#      print("택시타")
# elif money < taxi and money >=bus :
#      print("버스타")
# elif money == 0:
#     if card:
#         print("카드로 택시나 버스타")
#     else:
#         print("카드 없음 걸어가")

#=========================
#
# a = [1,2,3]
# b = 1
# c = []
# for i in a:
#      if b == i:
#          pass
#      else:
#          c = c + [i]
# print(c)

#=================

# coffee = 10
# money = 300
# while True:
#     money = int(input("돈을 입력하시오"))
#
#     if money == 300:
#         print("커피가 나온다")
#         coffee = coffee - 1
#     elif money > 300:
#         print("커피를 준다. 그리고 거스름돈 %d을 준다" % (money - 300))
#         coffee = coffee -1
#     else:
#         print("돈이 부족하다 ")
#         print("남은 커피양은 %d" % coffee)
#     if coffee == 0:
#         print("커피 sold out")
#         break

    # print("커피 준다.")
    # coffee = coffee - 1
    # print("남은 커피양 %d개" % coffee)
    # if coffee == 0:
    #     print("sold out")
    #     break

# Q1============
# a = "Life is too short, you need python"
#
# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python") #you 가 있어서 false
# elif "shirt" not in a : print("shirt")  # 정답이고 밑에줄 실행하지 않음
# elif "need" in a : print("need")
# else: print("none")

# Q2 ============
# i = 1
# sum3 = 0
# while i < 1000:
#     if i % 3 == 0:
#         sum3 = sum3 + i
#     i += 1
# print(sum3)

# Q3 ============

# i = 0
# data = "*"
# while i < 5:
#     i += 1
#     print(data*i)

# Q4 =============
# for i in range(1,101):
#     print(i)


# Q5 ===================

# classA = [70, 60, 55, 75, 95, 90, 80, 85, 100]
# sum = 0
# for i in classA:
#     sum = sum + i
#
# print(sum/len(classA))

# # Q6 =================
numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

result = [n * 2 for n in numbers if n % 2 == 1]
#리스트안에 append를 쓰면 none 값 리턴이여서 리스트안에 요소를 추가하려면 n * 2로 쓴다

print(result)
