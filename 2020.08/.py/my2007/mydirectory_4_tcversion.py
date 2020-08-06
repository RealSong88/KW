def transform_data(param):
    data = []
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        temp_list = line1.split(",")
        # data = []
        for i in range(int(len(temp_list) / 2)):
            data.append([temp_list[i * 2], int(temp_list[i * 2 + 1])])
    return data


# print(transform_data('my_directory\\data2.txt'))

report_data = []


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


make_report([['a', 1], ['b', 1], ['c', 3], ['b', 4]])
print(report_data)
make_report([['c', 1], ['r', 1], ['b', 3], ['b', 4]])
print(report_data)
