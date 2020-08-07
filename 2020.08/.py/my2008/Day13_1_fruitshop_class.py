import os


class ReadDirData:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.files_path = []
        self.read_dir()
        self.read_data()
        self.data_list = []

    def read_dir(self):
        with os.scandir(self.dir_path) as entries:
            for entry in entries:
                # print(entry.name)
                self.files_path.append(f"{self.dir_path}/{entry.name}")
                # print(files_path)

    def read_data(self):
        self.data_list = []
        for i in self.files_path:
            with open(i, "r", encoding="utf8") as f:
                line = f.readline()
                self.data_list.append(line)


myData = ReadDirData('e:/realsong/pycharmprojects/jump/practice/200803')
print(myData.dir_path)
print(myData.files_path)
myData.read_data()
print(myData.data_list)
