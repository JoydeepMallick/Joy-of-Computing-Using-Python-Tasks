#flipping the image

from PIL import Image

img = Image.open("obtained.png") # in default directory
#transposing --> mirror to actual image
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT) # IMAGE IN MATRIX FORMAT

#save it to a file in human understandable format

transposed_img.save("corrected.png")
print("Done flipping")

