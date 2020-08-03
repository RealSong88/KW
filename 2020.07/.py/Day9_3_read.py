import os


# 특정경로에 있는 파일들을 읽고 그 내용을 변수에 저장후 콘솔에 출력하는 함수
def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        line2 = f.readline()
        # print(line1)
        return line1


# 특정경로에 있는 파일들을 읽고 파일 제목을 출력하고
with os.scandir('E:/RealSong/PycharmProjects/jump/practice') as entries:
    for entry in entries:
        print(entry.name)
        print(read_data('E:/RealSong/PycharmProjects/jump/practice\\%s' % entry.name))
