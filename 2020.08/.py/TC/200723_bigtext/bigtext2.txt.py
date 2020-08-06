# 표시할 요소를 분해하여 변수로 만든다
df = "*****"
dl = "*    "
dr = "    *"
de = "     "
db = "*   *"

big_font_0 = "%s\n%s\n%s\n%s\n%s" % (df, db, db, db, df)
big_font_1 = "%s\n%s\n%s\n%s\n%s" % (dr, dr, dr, dr, dr)
big_font_2 = "%s\n%s\n%s\n%s\n%s" % (df, dr, df, dl, df)
big_font_3 = "%s\n%s\n%s\n%s\n%s" % (df,dr,df,dr,df)
big_font_4 = "%s\n%s\n%s\n%s\n%s" % (db,db,df,dr,dr)
big_font_5 = "%s\n%s\n%s\n%s\n%s" % (df,dl,df,dr,df)
big_font_6 = "%s\n%s\n%s\n%s\n%s" % (df,dl,df,db,df)
big_font_7 = "%s\n%s\n%s\n%s\n%s" % (df,db,dr,dr,dr)
big_font_8 = "%s\n%s\n%s\n%s\n%s" % (df,db,df,db,df)
big_font_9 = "%s\n%s\n%s\n%s\n%s" % (df,db,df,dr,dr)

big_font_d = "%s\n%s\n%s\n%s\n%s" % (de,de,df,de,de)
big_font_t = "%s\n%s\n%s\n%s\n%s" % (dr,dr,de,dr,dr)

big_font = [
    big_font_0, big_font_1, big_font_2, big_font_3, big_font_4, big_font_5,
    big_font_6, big_font_7, big_font_8, big_font_9, big_font_d, big_font_t
]


date = "2002-06-23"

# for i in date:
#     if i == "-":
#         print(big_font[10])
#     elif i == ":":
#         print(big_font[11])
#     else:
#         # "2" -> 2
#         i = int(i)
#         print(big_font[i])

# 가로로 출력하기
print("*"*59)
# *....\n*....
# \n을 하나의 문자로 계산
for i in [5,11,17,23,29]:
    data = ""
    for j in date:
        if j == "-":
            data = data + big_font[10][i-5:i] + " "
        elif j == ":":
            data = data + big_font[11][i-5:i] + " "
        else:
            # "2" -> 2
            j = int(j)
            data = data + big_font[j][i-5:i] + " "
    print(data)

print("*"*59)