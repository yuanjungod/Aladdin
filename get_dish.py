import pandas

ftrain = open("dict_dict.txt", "w")
a = pandas.read_csv("/Users/happy/Downloads/全量标准菜.csv")

for i in a['dim_dish_second_dish.normal_dish']:
    # i = i.decode("utf-8").encode("utf-8")
    ftrain.write("%s dish\n" % i)
    ftrain.flush()
ftrain.close()
