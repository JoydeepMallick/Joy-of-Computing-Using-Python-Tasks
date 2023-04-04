import cv2

#read image
img=cv2.imread("crime.png")

#Preparation for CLAHE
clahe = cv2.createCLAHE()

#WORKS BETTER IF IMAGE IS BLACK AND WHITE
#CONVERTING image to gray scale image

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply enhancement
enh_img = clahe.apply(gray_img)

#save it in a file
cv2.imwrite("enhanced.png", enh_img)

print("DOne enhancing")
