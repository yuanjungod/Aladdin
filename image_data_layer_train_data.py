import os
import random

root_folder = "/alidata/home/yuanjun/data/train_data/train/"


def random_choice(image_folder_files, count):
    if len(image_folder_files) < count:
        print("len(image_folder_files) must > count")
    choice_list = set()
    index_list = set(range(len(image_folder_files)))
    for i in range(count):
        index_list = index_list - choice_list
        choice_list.add(random.choice(list(index_list)))
    return choice_list


def train_data():
    train_txt = open("train.txt", "w+")
    image_folders = os.listdir(root_folder)
    count = 0
    while True:
        if count % 200 == 0:
            print(count)
        image_folder = random.choice(image_folders)
        image_folder_files = os.listdir(os.path.join(root_folder, image_folder))
        if len(image_folder_files) > 3:
            # begin = random.choice(range(len(image_folder_files)-3))
            for i in random_choice(image_folder_files, 3):
                train_txt.write("%s %s\n" % (os.path.join(image_folder, image_folder_files[i]), image_folder))
        else:
            for i in range(len(image_folder_files)):
                train_txt.write("%s %s\n" % (os.path.join(image_folder, image_folder_files[i]), image_folder))
        count += 1
        if count > 2000000:
            break
    train_txt.close()


def val_data():
    val_txt = open("val.txt", "w+")
    image_folders = os.listdir(root_folder)
    count = 0
    while True:
        if count % 200 == 0:
            print(count)
        image_folder = random.choice(image_folders)
        image_folder_files = os.listdir(os.path.join(root_folder, image_folder))
        if len(image_folder_files) > 3:
            for i in random_choice(image_folder_files, 3):
                val_txt.write("%s %s\n" % (os.path.join(image_folder, image_folder_files[i]), image_folder))
        else:
            for i in range(len(image_folder_files)):
                val_txt.write("%s %s\n" % (os.path.join(image_folder, image_folder_files[i]), image_folder))
        count += 1
        if count > 200000:
            break
    val_txt.close()


val_data()

