class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def minus(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


# str = input("연산을 입력하시오>")
# sign = ["+", "-", "*". "/"]
# num = []
# 2+1을 입력했을때
# for i in str:
#     for j in sign:
#         if j != i :
#             num.append(i)
#
#
#
