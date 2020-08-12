class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result


a = FourCal(7, 0)
print(a.add())
print(a.mul())
print(a.div())
b = MoreFourCal(4, 0)

print(b.div())