# Required Libraries
import cv2
from os import listdir
from os.path import isfile, join
import numpy
 

mypath="C:\Users\anind\Downloads\MTP\images"


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
 
# Iterate through every image
# and resize all the images.
for n in range(0, len(onlyfiles)):
 
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
 
    # Load the image in img variable
    img = cv2.imread(path, 1)
    resized_dimensions = (640, 360)
 
    # Create resized image using the calculated dimensions
    resized_image = cv2.resize(img, resized_dimensions,interpolation=cv2.INTER_AREA)
    name = './output/' +  str(n) + '_resized.jpg'
     
    # Save the resized image in Output Folder
    cv2.imwrite(name, resized_image)
 
print("Resized Images Successfully")