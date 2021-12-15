import os
import cv2
from PIL import Image

root = "D:\\VSD\\ViSha\\ViSha_data\\train\\labels"  #to be modified
fps = 30

file_url=[]
dir_url=[]
for root , dirs, files in os.walk(root):
    # for dir in dirs:
    #     print(dir)
    for dir in dirs:
        # print(file)
        dir_url.append(os.path.join(root, dir))
    for file in files:
        # print(file)
        file_url.append(os.path.join(root, file))

# print(file_url)
# print(dir_url)
# print(file_url[1].split("\\")[-2])
# os.system("pause")
for filedir in dir_url:
    name = filedir.split("\\")[-1]
    root = "D:\\VSD\\ViSha\\ViSha_data\\train\\labels" #to be modified
    # print(root)
    video_dir = root + "\\" + name + ".avi"
    print(video_dir)
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')  # opencv3.0
    im = Image.open(os.path.join(filedir, "00000001.png"))  # 返回一个Image对象 #to be modified
    # print('宽：%d,高：%d' % (im.size[0], im.size[1]))
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, (im.size[0], im.size[1]))#to be modified
    for root, dirs, images in os.walk(filedir):

        for image in images:

            # print(filename)
            im_name = os.path.join(root, image)
            # print(im_name)
            frame = cv2.imread(im_name)
            videoWriter.write(frame)


