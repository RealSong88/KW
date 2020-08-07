class Smartphone:
    """
    Smartphone Class
    """

    def __init__(self, brand, details):
        self._brand = brand
        self._details = details

    def __str__(self):
        return f'str : {self._brand} - {self._details}'

    def __repr__(self):
        return f'repr : {self._brand} - {self._details}'

    def detail_info(self):
        print(f'Current Id : {id(self)}')
        print(f'Smartphone Detail Info : {self._brand} {self._details.get("price")}')

Smartphone1 = Smartphone('Iphone', {'color': 'White', 'price': 10000})
Smartphone2 = Smartphone('Galaxy', {'color': 'Black', 'price': 8000})
Smartphone3 = Smartphone('Blackberry', {'color': 'Silver', 'price': 6000})

Smartphone2.detail_info()

print(Smartphone2._brand)
print(Smartphone2._details)

# print(Smartphone1.__class__, Smartphone2.__class__)
# # 부모는 같음
# print(id(Smartphone1.__class__) == id(Smartphone3.__class__))

a = 472
b = 385

print()