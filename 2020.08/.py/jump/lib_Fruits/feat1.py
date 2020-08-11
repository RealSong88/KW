def feat1(d_source):
    temp = d_source.split(",")
    data = []
    for i in range(len(temp)):
        if i % 2 == 1:
            data.append([temp[i-1], int(temp[i])])
    print("=" * 50)
    print(data)
    return data