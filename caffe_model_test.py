import os
import random
import cv2
from inferrence import *

date_root = "/alidata/home/yuanjun/data/train_data/train"
face_dir_list = os.listdir(date_root)

true_positive = 0
false_negative = 0
true_negative = 0
false_positive = 0

positive = 0
negative = 0


while True:
    left = random.choice(face_dir_list)
    right = random.choice(face_dir_list)
    if random.random() > 0.6:
        right = left

    pic1 = os.path.join(date_root, left, random.choice(os.listdir(os.path.join(date_root, left))))
    pic2 = os.path.join(date_root, right, random.choice(os.listdir(os.path.join(date_root, right))))
    distance = get_distance(net, transformer, pic1, pic2)

    if left == right:
        positive += 1
    else:
        negative += 1

    if distance <= 0.9:
        if left == right:
            true_positive += 1
        else:
            false_positive += 1
    elif distance > 1:
        if left == right:
            false_negative += 1
        else:
            true_negative += 1

    if positive > 0 and negative > 0 and (positive+negative) % 100 == 0:

        print("true positive rate: %s" % ((1.0*true_positive)/(true_positive+false_positive)))
        print("false positive rate: %s" % ((1.0*false_positive)/(true_positive+false_positive)))
        print("positive recall: %s" % (1.0*true_positive/positive))

        print("#################################################################################")

        print("true negative rate: %s" % ((1.0*true_negative)/(true_negative+false_negative)))
        print("false negative rate: %s" % ((1.0*false_negative)/(true_negative+false_negative)))
        print("negative recall: %s" % (1.0*true_negative/negative))








