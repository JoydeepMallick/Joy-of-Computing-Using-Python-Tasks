import scipy.misc
from PIL import Image
import numpy as np
import random

#import imageio as iio
#import matplotlib.pyplot as plt
#import cv2

img = scipy.misc.imread("india map.png")
#img = iio.read("india map.png")
#img = plt.imread("india map.png")
#img = cv2.imread("india map.png")

count_pun, count_in, count = 0, 0, 0

while(count <= 10000): # greater iterations better results
    #in order to get random values for each pixel we need the dimaneison of the
    #image which can be founs in the properties of image in details section
    
    # in our case width x height (length x breadth in video) = 605 x 676
    x = random.randint(0, 675) # in python x resembles height
    y = random.randint(0, 604) # in python y resembles width
    '''in general we consider horizontal * vertical dimensions 
    but in python x*y is considered as vertical * horizontal
    i.e. flipped'''

    z = 0 # our image is 2d 
    if img[x][y][z] == 60 :
        count += 1
        count_in += 1
    else:
        if img[x][y][z] == 80:
            count += 1
            count_pun += 1
area_pun =(count_pun/count_in) * 3287263
print(area_pun)

