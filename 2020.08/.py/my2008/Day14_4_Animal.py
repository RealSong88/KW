class Animal:
    def __init__(self):

        self.type = "동물"

    def get_type(self):
        print(self.type)
        return self.type


class Human(Animal):
    def __init__(self, name = "nadayong"):
        self.name = name

    def bark(self):
        print("예~")


class Lion(Animal):
    def bark(self):
        print("어흥")


class Tiger(Animal):
    def bark(self):
        print("으르렁")


class Cat(Tiger):
    def bark(self):
        print("야옹")


# Animal의 함수 type_str, eat() 애니멀을 상속받은 Tiger 는 함수 bark("으르렁") tiger가 상속받은 캣


T1 = Tiger()
print(T1.type)

T1.bark()

C1 = Cat()
print(C1.type)

C1.bark()

H1 = Human()
print(H1.name)
H1.bark()