import os
import random
import cv2
from inferrence import *

date_root = "/Users/happy/Downloads/train_data/train"
face_dir_list = os.listdir(date_root)
total_count = 1
right_count = 1
same_people_right_count = 1
same_people_count = 1
diff_people_right_count = 1
diff_people_count = 1
while True:
    left = random.choice(face_dir_list)
    right = random.choice(face_dir_list)
    if random.random() > 0.6:
        right = left
    if left == right:
        if total_count % 30 == 0:
            print("same people")
        pic1 = os.path.join(date_root, left, random.choice(os.listdir(os.path.join(date_root, left))))
        pic2 = os.path.join(date_root, right, random.choice(os.listdir(os.path.join(date_root, right))))

        distance = get_distance(net, transformer, pic1, pic2)
        same_people_count += 1
        if total_count % 30 == 0:
            print(distance)
        total_count += 1
        if distance <= 0.9:
            right_count += 1
            same_people_right_count += 1

    elif left != right:
        if total_count % 30 == 0:
            print("different people")
        pic1 = os.path.join(date_root, left, random.choice(os.listdir(os.path.join(date_root, left))))
        pic2 = os.path.join(date_root, right, random.choice(os.listdir(os.path.join(date_root, right))))
        distance = get_distance(net, transformer, pic1, pic2)
        diff_people_count += 1
        if total_count % 30 == 0:
            print(distance)
        total_count += 1
        if distance > 0.9:
            right_count += 1
            diff_people_right_count += 1
    if total_count % 30 == 0:
        print("total right rate", total_count, right_count, (right_count*1.0)/total_count)
        print("same people right rate", same_people_count, same_people_right_count, (same_people_right_count*1.0)/same_people_count)
        print("diff people right rate", diff_people_count, diff_people_right_count, (diff_people_right_count*1.0)/diff_people_count)
        print("#####################################################################################")





