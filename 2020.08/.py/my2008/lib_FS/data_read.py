class MySales:
    def __init__(self, files_path):
        self.files_path = files_path
        self.sale_list = []
        self.transform()
    # files_path 를 받아서 2차원배열로 품목과 수량을 sale_list 에 담는 함수
    def transform(self):
        with open(self.files_path, 'r', encoding='utf8') as f:
            line = f.readline()
            temp = line.split(",")
            for i in range(int(len(temp)/2)):
                self.sale_list.append([temp[i * 2], int(temp[(i * 2) + 1])])

    # def read_data(files_path):
    #     with open(files_path, 'r', encoding='utf8') as f:
    #         line = f.readline()
    #     return line



a = MySales('e:/realsong/pycharmprojects/jump/practice/200803/S1_20200805.txt')
print(a.sale_list)