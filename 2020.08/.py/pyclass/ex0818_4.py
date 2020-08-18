"""
다형성(Pylymorphism)
같은 모양의 코드가 다른 동작을 하는 것
파이썬은 동적인 방식의 다형성
"""


class Korean():
    def greeting(self):
        print("안녕하세요")


class American():
    def greeting(self):
        print("Hello")


def sayhello(people):
    people.greeting()


kim = Korean()
john = American()

sayhello(kim)
sayhello(john)
