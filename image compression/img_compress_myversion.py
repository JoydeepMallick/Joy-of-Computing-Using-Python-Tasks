import numpy

from PIL import Image

im = Image.open("lena_gray.jpg")

pixelMap = im.load()

I = numpy.asanyarray(Image.open('lena_gray.jpg'))
# above converts image into numpy matrix values
#print(I)


img = Image.new(im.mode, im.size) # genrated a blank img object of same dimesions and mode
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
            pixelNew[i,j] = (pixelMap[i,j]//32) * 32

img.save('lena_3.jpg')

J = numpy.asanyarray(Image.open("lena_3.jpg"))
print(J)
