import cv2

img = cv2.imread("lena.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("lena_gray.jpg", gray_image)

print("Done making it grayscale!!!")
