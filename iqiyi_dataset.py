# -*- coding: utf-8 -*-
import os
import cv2
import face_recognition


class IqiyiDataSet(object):

    def __init__(self, root_fold, train_data_path, number_of_times_to_upsample=1):
        self.root_fold = root_fold
        self.number_of_times_to_upsample = number_of_times_to_upsample
        self.train_label_path = os.path.join(root_fold, "train.txt")
        self.train_image_fold = os.path.join(root_fold, "IQIYI_VID_TRAIN")
        self.val_label_path = os.path.join(root_fold, "val.txt")
        self.val_image_fold = os.path.join(root_fold, "IQIYI_VID_VAL")
        self.train_data_path = train_data_path

    def detect_face(self, image):
        # face_locations = face_recognition.face_locations(image, self.number_of_times_to_upsample, model="cnn")
        face_locations = face_recognition.face_locations(image, self.number_of_times_to_upsample)
        print(face_locations)
        if len(face_locations) == 1:
            return image[face_locations[0][0]: face_locations[0][2], face_locations[0][3]: face_locations[0][1]]
        return None

    def create_train_data(self):
        if not os.path.exists(os.path.join(self.train_data_path, "train")):
            os.mkdir(os.path.join(self.train_data_path, "train"))
        with open(self.train_label_path) as f:
            for i in f:
                video_name, label = i.split(" ")
                print(os.path.join(self.train_image_fold, video_name), label)
                cap = cv2.VideoCapture(os.path.join(self.train_image_fold, video_name))
                count = 0
                while True:
                    ret, frame = cap.read()
                    if frame is not None:
                        face = self.detect_face(frame)
                        if face is None:
                            continue
                        if not os.path.exists(os.path.join(self.train_data_path, "train/%s" % label)):
                            print(os.path.join(self.train_data_path, "train/%s" % label))
                            os.mkdir(os.path.join(self.train_data_path, "train/%s" % label))
                        print(count)
                        cv2.imwrite(os.path.join(self.train_data_path, "train/%s" % label, "train_%s.jpg" % count), face)
                        count += 1
        with open(self.val_label_path) as f:
            for i in f:
                video_name, label = i.split(" ")
                print(os.path.join(self.train_image_fold, video_name), label)
                cap = cv2.VideoCapture(os.path.join(self.val_image_fold, video_name))
                count = 0
                while True:
                    ret, frame = cap.read()
                    if frame is not None:
                        face = self.detect_face(frame)
                        if face is None:
                            continue
                        if not os.path.exists(os.path.join(self.train_data_path, "train", label)):
                            print(os.path.join(self.train_data_path, "train", label))
                            os.mkdir(os.path.join(self.train_data_path, "train", label))
                        print(count)
                        cv2.imwrite(os.path.join(self.train_data_path, "train", label, "val_%s.jpg" % count), face)
                        count += 1


if __name__ == "__main__":
    iqiyi_dataset = IqiyiDataSet("/Users/happy/Downloads/IQIYI_VID_DATA_Part1", "/Users/happy/Downloads/train_data")
    iqiyi_dataset.create_train_data()
    # cap = cv2.VideoCapture(0)
    # count = 0
    # while True:
    #     ret, frame = cap.read()
    #     face = iqiyi_dataset.detect_face(frame)
    #     if face is None:
    #         continue
    #     cv2.imshow("me", face)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break




