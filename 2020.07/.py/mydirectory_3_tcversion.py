import os


# 폴더를 읽고 파일경로와 파일제목을 transform_data 에 넣음
def dir_list(param_str):
    with os.scandir(param_str) as entries:
        for entry in entries:
            file_name = entry.name
            print(file_name)
            print(transform_data("%s\\%s" % (param_str, file_name)))
            t_list = transform_data("%s\\%s" % (param_str, file_name))  # 여기 다시 이해해야함
            make_report(t_list)


def transform_data(param):
    data = []
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        temp_list = line1.split(",")
        # data = []
        for i in range(int(len(temp_list) / 2)):
            data.append([temp_list[i * 2], int(temp_list[i * 2 + 1])])
    return data


report_data = [] # 중복확인함수와 리포트만드는함수 사용하기 위해


def check_dupl(item_list):
    for i in range(len(report_data)):
        if report_data[i][0] == item_list[0]:
            return True, i
    return False, None


def make_report(param_list):
    for i in param_list:
        is_dupl, no_dupl = check_dupl(i)
        if is_dupl:
            report_data[no_dupl][1] = report_data[no_dupl][1] + i[1]
        else:
            report_data.append(i)

        with open("make_report.csv", "w", encoding='utf8') as f:
            for i in report_data:
                # print("%s, %s\n" % (i[0], i[1]))
                f.write("%s, %s\n" % (i[0], i[1]))
    print(report_data)

dir_list('my_directory')

# print(transform_data('my_directory\\data2.txt'))
