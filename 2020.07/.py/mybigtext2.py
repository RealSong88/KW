df = "*****"
dr = "    *"
dl = "*    "
db = "*   *"
de = "     "

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
big_font_0, big_font_1, big_font_2, big_font_3, big_font_4,
big_font_5, big_font_6, big_font_7, big_font_8, big_font_9,
big_font_d, big_font_t
]



date = "2020-07-23"

for i in date:
    if i == "-":
        print(big_font[10])
    elif i == ":":
        print(big_font[11])
    else:
        i = int(i)
        print(big_font[i])

