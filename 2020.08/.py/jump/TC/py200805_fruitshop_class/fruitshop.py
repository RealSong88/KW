from TC.py200805_fruitshop_class.mydir import MyDir
from TC.py200805_fruitshop_class.mysale import MySale

my_dir_0701 = MyDir("E:/RealSong/PycharmProjects/jump/TC/py200805_fruitshop_class/200701")
print("{}/{}".format(my_dir_0701.dir, my_dir_0701.files[0]))
print(my_dir_0701.files)


my_dir_0701_list = []
# MySale 이란 객체에 sale_list를 뽑아내야한다.
for i in my_dir_0701.files:
    # my_dir_0701_list.append(MySale("{}/{}".format(my_dir_0701.dir,i)).sale_list)
    my_dir_0701_list += MySale("{}/{}".format(my_dir_0701.dir, i)).sale_list
print(my_dir_0701_list)



# my_dir_0701_list.append(MySale("{}/{}".format(my_dir_0701.dir, my_dir_0701.files[0])))
# my_dir_0701_list += MySale("{}/{}".format(my_dir_0701.dir, my_dir_0701.files[0])).transform_data()
#
# print(my_dir_0701_list)


#my_dir_0702 = MyDir("200702")
#print(my_dir_0702.files)
#my_dir_0703 = MyDir("200703")
#print(my_dir_0703.files)
