#파일 만들고, 읽음
# f = open("e:/realsong/test.txt", "w")
# for i in range(1,11):
#     data = "%2d번째 test입니다. \n" % i
#     f.write(data)
# f.close()


# readline() 한줄 식 읽는다.
# f = open("e:/realsong/test.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# readline() 을 반복문을 사용해서 데이터가 없을 때까지 읽음
# f = open("e:/realsong/test.txt", 'r')
# while True:
#     line = f.readline() #커서가 이동한다.
#     if not line: break
#     print(line)
# f.close()

# readlines()는 모든줄을 읽어 각각의 줄을 요소로 갖는 리스트를 생성
f = open("e:/realsong/test.txt", 'r')
lines = f.readlines()
print(lines)

