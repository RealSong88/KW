# filter 함수
#
# def positive(x):
#     return x > 0
#
# print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# eval 함수 ""안에 있는 문자열이나 숫자를 연산한다.
# print(eval(input("계산식을 입력하라 ('='은 입력하지않는다.)>>>")))



with open('e:/realsong/pycharmprojects/jump/유튜버1.txt', encoding='utf8') as f:
    line = f.read()
    print(line)

# dir 함수는 자료형에서 쓸수있는 변수나 함수를 보여줌
print(dir("문자열?"))