import os


# 폴더를 스캔해서 폴더경로와 그 안에 파일명, 파일경로를 저장하는 클래스
class ReadDir:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.files_path = []
        self.files_name = []
        self.read_dir()

    def read_dir(self):
        with os.scandir(self.dir_path) as entries:
            for entry in entries:
                items = entry.name
                self.files_path.append(self.dir_path + "/" + items)
                self.files_name.append(items)
        # return self.file_path

    # dir_path 경로에 txt파일 생성
    def create_txt(self):
        with open("{}/untitled.txt".format(self.dir_path), 'w') as f:
            f.write("내용은 차차...")

    # def read_data(self):
    #     for i in self.files_path:
    #        with open(i, 'r', encoding='utf8') as f:
    #         line = f.readline()
    #         print(line)


# mydir = ReadDir('e:/realsong/pycharmprojects/jump/practice/200803')
# print("mydir 실행!", mydir.read_dir())
# print("탐색경로 :", mydir.dir_path)
# print("경로의 파일이름 :", mydir.files_name)
# print("파일의 전체경로 :", mydir.files_path)

# mydir.read_data()
