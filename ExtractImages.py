# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:41:13 2021

@author: pallavi
"""

# Importing  necessary libraries
import cv2
import os
from os import walk

mypath = r"C:\Users\anind\Downloads\MTP\Videos"

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
# printing file names in the video folder
print(f)

for videoFile in f:
    # Read the video from the specified path
    cam = cv2.VideoCapture(mypath + "\\" + videoFile)
    videoFileName = videoFile[:-4]
    try:

        # creating a folder named images for storing extracting images
        if not os.path.exists('images'):
            os.makedirs('images')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    fps = 25
    # Get value of FPS for the video
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
    if int(major_ver) < 3:
        fps = cam.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second for video is: {0}".format(fps))
    else:
        fps = cam.get(cv2.CAP_PROP_FPS)
        print("Frames per second for video is: {0}".format(fps))

    # frame
    currentframe = 0
    count = 0

    while (True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            count += 1
            if count % (fps * 10) == 0:
                # name of extracted image frame from the video
                name = './images/' + str(videoFileName) + '_frame' + str(currentframe) + '.jpg'

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter for the number of frames being created
                currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
