import os
from random import randint


# 랜덤의 판매아이템과, 수량생성
def create_sale_data():
    sales_count = (3, 6)
    sale_name = (97, 101)
    sale_count = (1, 5)

    result = ""
    # 판매횟수를 3 ~ 6 까지 랜덤으로 정함
    for sc in range(randint(sales_count[0], sales_count[1])):
        s = ','
        # 처음 result 에 , 를 뺌
        if not result:
            s = ""
            # result 에 "," , 랜덤으로 a ~ e 의 문자, 랜덤으로 판매수량을 대입한다.
        result += "{}{},{}".format(s, chr(randint(sale_name[0], sale_name[1])),
                                   randint(sale_count[0], sales_count[1]))
    return result
print(create_sale_data())

def create_file(file_nm, data):
    # n = 0
    # while os.path.isfile(file_nm):
    #     n += 1
    #     idx = file_nm.index('.txt')
    #     if n > 1:
    #         idx2 = file_nm.index('(')
    #         file_nm = "{}({}){}".format(file_nm[:idx2], n, file_nm[idx:])
    #     else:
    #         file_nm = "{}({}){}".format(file_nm[:idx], n, file_nm[idx:])

    with open(file_nm, 'w') as f:
        f.write(data)


def create_myfile(file_name, data):
    # 파일이름과 데이터를 넣므면 파일 생성
    with open(file_name, 'w') as f:
        f.write(data)


# create_file("ilsan.txt", "a,1,b,2,c,3,a,2")

def do_init():
    # 기본 폴더 이름
    base_dir = "mySource"
    # 지역 샘플 이름으로 파일명과 처음 파일 내용
    branchess = ("gangnam", 'silim', 'mapo', 'wonhyo', 'daerim', 'guro')
    # 날짜 별로 폴더 생성
    dates = ('20200720', '20200802', '20200815')

    for date in dates:
        # path 에 기본폴더와 날짜별폴더명 대입
        path = base_dir + "/{}".format(date)
        # os.makedirs 로 하위폴더까지 생성
        os.makedirs(path, exist_ok=True)

        for br in branchess:
            # text 변수에 지역 샘플 이름 대입
            text = "{}\n".format(br)
            # 랜덤의 판매아이템과 수량을 text 변수에 대입
            text += create_sale_data()
            # 변수에  파일경로/지역샘플이름을 대입
            path_file = '{}/{}.txt'.format(path, br)
            # 함수에 값을 대입하여 파일 생성
            create_myfile(path_file, text)


# os.makedirs("mySource//{}", exist_ok=True)
if __name__ == "__main__":
    do_init()
