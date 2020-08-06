# 예외처리 예제

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
#

#
# try:
#     4 / 0
#     a = [1, 2]
#     print(a[3])
#
# except (ZeroDivisionError, IndexError) as e:
#     print(e)


#==========================================================

class MyError(Exception):
    pass


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

#
# say_nick("천사")
# say_nick("바보")

try:
    say_nick("천사")
    say_nick("바보")
except MyError:  # try except 을 사용해서 MyError를 예외처리 시킴
    print("안돼 임마")

# 다시
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
