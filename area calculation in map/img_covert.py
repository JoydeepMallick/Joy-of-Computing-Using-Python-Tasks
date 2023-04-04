from PIL import Image

im = Image.open("test1.png")
rgb_im = im.convert("RGB")
r, g, b = rgb_im.getpixel((1, 1))
# here x and y cordinates denotes which cell we require to get the rgb values
print(r, g, b)

r, g, b = rgb_im.getpixel((150, 1))
print(r, g, b)
