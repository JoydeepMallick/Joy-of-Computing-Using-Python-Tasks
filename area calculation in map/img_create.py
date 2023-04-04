import numpy as np
from PIL import Image
width, height = 5, 4

array = np.zeros([height, width, 3], dtype = np.uint8)
# datatype is unassigned 8 bit integers
# each pixel contain 3 vlues for RGB hence we write 3 in the dimension of the
# array
# the image formed is only back since all values are black intially

img = Image.fromarray(array)

img. save("test.png")

array1 = np.zeros([100, 200, 3], dtype = np.uint8)
array1[:, :100] = [255, 128, 0] # orange, in first 99 columns for all rows
array1[:, 100:] = [0, 0, 255] # blue, in 100 to rest columns for all rows

img = Image.fromarray(array1)
img. save("test1.png")

