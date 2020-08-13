import os


# def search(dirname):
#     filenames = os.listdir(dirname)
#     print(filenames)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#         # ext = os.path.splitext(full_filename)[-1]
#         ext = full_filename[-3:]
#         if ext == '.py':
#             print(full_filename)
#
# search("c:/realsong/documents/pycharmprojects/mydoit")

# def search2(dirname):
#     with os.scandir(dirname) as entries:
#         for entry in entries:
#             print(dirname + entry.name)
#
# search2("c:/")


# def search3(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         # print(filenames)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search3(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if full_filename.find("venv") == -1: # 문자열 'venv' 가 없을 경우
#                 # if 'game' in full_filename: # 문자열에 'game' 이 있으면 True
#                     if ext == '.py':
#                         print(full_filename)
#     except PermissionError:
#         pass
#
# search3("c:/realsong/documents/pycharmprojects/mydoit")

def search4(dirname):
    for(path, dir, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py':
                if "venv" not in path:
                    print("%s%s" % (path, filename))



search4("c:/realsong/documents/pycharmprojects/mydoit")