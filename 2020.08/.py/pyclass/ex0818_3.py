"""
인스턴스를 속성으로 사용하기
큰 클래스의 일부분을 잘라내 별도의 클래스로 만들어 사용한다.
"""


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_read = 0

    def get_car_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batterry = Battery()


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a : " + str(self.battery_size) + "-kWh battery.")
