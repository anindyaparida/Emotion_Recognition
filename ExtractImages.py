# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:41:13 2021

@author: pallavi
"""

# Importing all necessary libraries
import cv2
import os
from os import walk
from duplicateRem import DuplicateRemover

mypath=r"C:\Users\anind\Downloads\MTP\Videos"

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
  f.extend(filenames)
  break
# printing file names
print(f)  

videoNumber=0

for videoFile in f:
  # Read the video from specified path
  cam = cv2.VideoCapture(mypath+"\\"+videoFile)
  videoNumber=videoNumber+1  
  try:
        
      # creating a folder named data
      if not os.path.exists('images'):
          os.makedirs('images')
    
  # if not created then raise error
  except OSError:
      print ('Error: Creating directory of data')
      
  fps = 25
  
  (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
  # With webcam get(CV_CAP_PROP_FPS) does not work.
  # Let's see for ourselves.
  if int(major_ver)  < 3 :
      fps = cam.get(cv2.cv.CV_CAP_PROP_FPS)
      print("Frames per second for video is: {0}".format(fps))
  else :
      fps = cam.get(cv2.CAP_PROP_FPS)
      print("Frames per second for video is: {0}".format(fps))
      
  # frame
  currentframe = 0
  count = 0
  
  while(True):
        
      # reading from frame
      ret,frame = cam.read()
    
      if ret:
          count +=1
          if count%(fps*20) == 0:
              # if video is still left continue creating images
              name = './images/videoNumber'+str(videoNumber)+'frame' + str(currentframe) + '.jpg'
              #print ('Cr eating...' + name)
        
              # writing the extracted images
              cv2.imwrite(name, frame)

              # increasing counter so that it will
              # show how many frames are created
              currentframe += 1

      else:
          break

  dirname = r"C:\Users\anind\Downloads\MTP\images"

  # Remove Duplicates
  dr = DuplicateRemover(dirname)
  dr.find_duplicates()
    
  # Release all space and windows once done
  cam.release()
  cv2.destroyAllWindows()
