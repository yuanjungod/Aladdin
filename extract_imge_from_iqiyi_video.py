import os
# ffmpeg -i /Volumes/Seagate\ Expansion\ Drive/face/IQIYI/IQIYI_VID_DATA_Part1/IQIYI_VID_TRAIN/IQIYI_VID_TRAIN_0000001.mp4 -vf fps=fps=8/1 -q 0 /Volumes/Seagate\ Expansion\ Drive/face/IQIYI/test/%06d.jpg
root_path = "/Volumes/Seagate Expansion Drive/face/IQIYI/IQIYI_VID_DATA_Part1/IQIYI_VID_VAL"

video_paths = os.listdir(root_path)

for video_path in video_paths:
    if not os.path.exists("/Volumes/Seagate Expansion Drive/face/IQIYI/images_part1/val/%s" % video_path.split(".")[0]):
        os.mkdir("/Volumes/Seagate Expansion Drive/face/IQIYI/images_part1/val/%s" % video_path.split(".")[0])
    cmd = "ffmpeg -i /Volumes/Seagate\ Expansion\ Drive/face/IQIYI/IQIYI_VID_DATA_Part1/IQIYI_VID_VAL/" + video_path + \
          " -vf fps=fps=8/1 -q 0 /Volumes/Seagate\ " \
          "Expansion\ Drive/face/IQIYI/images_part1/val/" + video_path.split(".")[0] + "/%06d.jpg"
    print(cmd)

    os.system(cmd)
    # exit()