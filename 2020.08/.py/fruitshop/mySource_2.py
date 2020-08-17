import os
from random import randint, randrange


def create_data():
    sale_items = ('apple', 'grape', 'melon', 'tomato', 'mango')
    # 몇가지의 품목을 판매할지의 범위
    sales_count = (3, 6)
    # 품목의 수량 범위
    sale_count = (1, 5)
    # 데이터 담을 변수
    result = ""
    for i in range(randint(sales_count[0], sales_count[1])):
        s = ","
        if not result:
            s = ""
        result += "{}{},{}".format(s, sale_items[randrange(len(sale_items))],
                                   randint(sale_count[0], sale_count[1]))

    return result


def create_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def do_init():
    # 기본 폴더 경로
    base_dir = 'createMysource'
    # 날짜별 폴더명
    dates = ['200731', '200802', '200803']
    # 지역 데이터 설정
    locals = ['sillim', 'guro', 'sadang', 'yongsan']

    for date in dates:
        # 기본 폴더 경로에 날짜별 폴더명까지 저장
        path = "{}/{}".format(base_dir, date)
        # os.makedirs 는 하위 폴더까지 생성 한다.
        os.makedirs(path, exist_ok=True)
        for local in locals:
            # data 변수에 지역명을 저장하고 줄바꿈
            data = "{}\n".format(local)
            # 추가로 랜덤한 아이템품목 및 수량 대입
            data += create_data()
            # 저장될 경로와 파일명 설정
            path_file = "{}/{}.txt".format(path, local)
            # 함수로 원하는 경로에 파일저장
            create_file(path_file, data)


if __name__ == '__main__':
    do_init()