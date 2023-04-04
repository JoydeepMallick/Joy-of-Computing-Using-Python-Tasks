import numpy

from PIL import Image

im = Image.open("lena_gray.jpg")

pixelMap = im.load()

I = numpy.asanyarray(Image.open('lena_gray.jpg'))
# above converts image into numpy matrix values
#print(I)


img = Image.new(im.mode, im.size)
# (image mode which type= grayscale here,image size)
#
pixelNew = img.load()

'''
8bits means 2 ^ 8 values
3 bits means 2 ^ 3 values

our mapping :-

 0 - 31 --> 0
 32 - 63 --> 1
 64 - 95 --> 2
 96 - 127 --> 3
 128 - 159 --> 4
 160 - 191 --> 5
 192 - 223 --> 6
 224 - 255 --> 7
'''

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixelMap[i, j] >= 0 and pixelMap[i, j] <= 31:
            pixelNew[i,j] = 0
        elif pixelMap[i, j] in range(32, 64): # 32 to 63
            pixelNew[i,j] = 1
        elif pixelMap[i, j] in range(64, 96): # 64 to 96
            pixelNew[i,j] = 2
        elif pixelMap[i, j] in range(96, 128): # 96 to 127
            pixelNew[i,j] = 3
        elif pixelMap[i, j] in range(128, 160): # 128 to 159 
            pixelNew[i,j] = 4
        elif pixelMap[i, j] in range(160, 192): # 160 to 191
            pixelNew[i,j] = 5
        elif pixelMap[i, j] in range(192, 224): # 192 to 223
            pixelNew[i,j] = 6
        elif pixelMap[i, j] in range(224, 226): # 224 to 255 
            pixelNew[i,j] = 7

img.save('lena_2.jpg')

J = numpy.asanyarray(Image.open("lena_2.jpg"))
print(J)
