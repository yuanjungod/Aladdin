from mxnet import recordio
import numpy as np
import cv2
import os
import traceback


path_imgidx = "/alidata/home/yuanjun/data/faces_ms1m_112x112/train.idx"
path_imgrec = "/alidata/home/yuanjun/data/faces_ms1m_112x112/train.rec"
save_path = "/alidata/home/yuanjun/data/ms1m"
imgrec = recordio.MXIndexedRecordIO(path_imgidx, path_imgrec, 'r')
s = imgrec.read_idx(0)
header, img = recordio.unpack(s)
print(header, img)
count = 0
while True:
    print(count)
    s = imgrec.read()
    if s is None:
        raise StopIteration
    header, img = recordio.unpack(s)
    try:
        image = np.asarray(bytearray(img), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        print(header)
        if not os.path.exists(os.path.join(save_path, str(int(header.label)))):
            os.mkdir(os.path.join(save_path, str(int(header.label))))
        cv2.imwrite(os.path.join(save_path, str(int(header.label)), "%s.jpg" % header.id), image)
        # cv2.imshow('URL2Image', image)
    except:
        # traceback.print_exc()
        print("except", header, img)
    # if cv2.waitKey(-1) & 0xFF == ord('a'):
    #     print "pressed a"
    count += 1

    # print(img)


