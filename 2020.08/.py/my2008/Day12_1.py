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

    def minus(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = FourCal(4, 2)
b = FourCal(7, 2)
c = MoreFourCal(4, 2)
d = SafeFourCal(9, 0)

print(a.first)
print(a.second)
print(a.add())
print(a.minus())
print(a.mul())
print(a.div())

print(b.first)
print(b.second)
print(b.add())
print(b.minus())
print(b.mul())
print(b.div())

print(id(a.first))
print(id(b.first))

print("=" * 50)
print(c.pow())
print(d.div())