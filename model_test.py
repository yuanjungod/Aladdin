import face_recognition
import os
import random
import cv2

date_root = "/Users/happy/Downloads/train_data/train"
face_dir_list = os.listdir(date_root)
total_count = 0
right_count = 0
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

        pic1_image = cv2.imread(pic1)
        pic2_image = cv2.imread(pic2)
        rgb_small_frame1 = pic1_image[:, :, ::-1]
        rgb_small_frame2 = pic2_image[:, :, ::-1]

        face_locations1 = face_recognition.face_locations(rgb_small_frame1, 1, model="cnn")
        # print("face", face_locations1)
        face_encodings1 = face_recognition.face_encodings(rgb_small_frame1, face_locations1, 10)

        face_locations2 = face_recognition.face_locations(rgb_small_frame2, 1, model="cnn")
        face_encodings2 = face_recognition.face_encodings(rgb_small_frame2, face_locations2, 10)
        # print("face encodings2", face_encodings2)
        if len(face_encodings1) == 0 or len(face_encodings2) == 0:
            continue
        total_count += 1
        if total_count % 30 == 0:
            print(face_recognition.face_distance(face_encodings1, face_encodings2[0]))
        if face_recognition.face_distance(face_encodings2, face_encodings2[0])[0] < 0.4:
            right_count += 1

    elif left != right:
        if total_count % 30 == 0:
            print("different people")
        pic1 = os.path.join(date_root, left, random.choice(os.listdir(os.path.join(date_root, left))))
        pic2 = os.path.join(date_root, right, random.choice(os.listdir(os.path.join(date_root, right))))
        pic1_image = cv2.imread(pic1)
        pic2_image = cv2.imread(pic2)

        rgb_small_frame1 = pic1_image[:, :, ::-1]
        rgb_small_frame2 = pic2_image[:, :, ::-1]

        face_locations1 = face_recognition.face_locations(rgb_small_frame1, 1, model="cnn")
        # print("face1", face_locations1)
        face_encodings1 = face_recognition.face_encodings(rgb_small_frame1, face_locations1, 10)

        face_locations2 = face_recognition.face_locations(rgb_small_frame2, 1, model="cnn")
        # print("face2 locations2", face_locations2)
        face_encodings2 = face_recognition.face_encodings(rgb_small_frame2, face_locations2, 10)
        # print("face2 encoding2", face_encodings2)
        if len(face_encodings1) == 0 or len(face_encodings2) == 0:
            continue
        total_count += 1
        if total_count % 30 == 0:
            print(face_recognition.face_distance(face_encodings1, face_encodings2[0]))
        if face_recognition.face_distance(face_encodings1, face_encodings2[0])[0] >= 0.4:
            right_count += 1
    if total_count % 30 == 0:
        print(total_count, right_count, (right_count*1.0)/total_count)
        print("#####################################################################################")





