# Q1 ================================

# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, val):
#         self.value += val
#
# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val
#
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
#
# print(cal.value)

# Q2 =====================

# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, val):
#         self.value += val
#
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100 :
#             self.value = 100
#         # return self.value
#
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)

# Q3 ========================
# all([1, 2, abs(-3)-3]) 리스트안에 하나라도 False 이면 False를 반환

# chr(ord('a') == 'a' ord함수는 아스키코드값 반환 chr함수는 아스키코드숫자를 문자로 변환 True



