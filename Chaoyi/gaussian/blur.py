import scipy
from scipy import misc
from scipy import ndimage
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import block_reduce
from PIL import Image
import os
import shutil
gaussian_counter = 0
def gaussian(name):
    f = cv2.imread(name)
    q = [1, 3, 5]
    t = [0.9, 1.1, 1.3, 1.2, 1.0]
    a = np.random.choice(q)
    b = np.random.choice(q)
    while (a == b and b == 1) or (a==b and b==5):
        b = np.random.choice(q)
    c = np.random.choice(t)
    blurred_f = cv2.GaussianBlur(f, (a, b), c)
    return blurred_f



def rename():
    file = []
    counter = 0
    f = os.listdir("selectedImage")
    for file in f:
        if '.jpg' in file:
            path = "selectedImage/" + file
            counter += 1
            shutil.copy(path,"high/" + str(counter) + ".jpg")
            blurred = gaussian(path)
            
            cv2.imwrite("low/" + str(counter) + ".jpg",blurred)
    
if __name__ == "__main__":
    rename()