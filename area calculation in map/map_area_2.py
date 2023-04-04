import random 
from PIL import Image

im = Image.open("india map.png")
rgb_im = im.convert("RGB")
count_in, count_pun, count = 0, 0, 0

while count <= 100000:
    x = random.randint(0, 675)
    y = random.randint(0, 604)
    z = 0
    r, g, b = rgb_im.getpixel((x, y))
    if r == 60:
        count_in += 1
        count += 1
    else :
        if r == 80:
            count_pun += 1
            count += 1

area_pun = (count_pun/count_in) * 3287263
print(area_pun)
