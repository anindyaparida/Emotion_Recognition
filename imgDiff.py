from diffimg import diff
import  os

IMAGES_DIR = "images"
def mk_img_path(f):
    return os.path.join(IMAGES_DIR, f)

IMG1 = mk_img_path("videoNumber1frame0.jpg")
IMG2 = mk_img_path("videoNumber1frame1.jpg")

# difference is defined by the average % difference between
# each of the channels (R,G,B,A?) at each pair of pixels Axy, Bxy

percentage = diff(IMG1, IMG2, delete_diff_file=True)
print('Difference is :',  percentage)