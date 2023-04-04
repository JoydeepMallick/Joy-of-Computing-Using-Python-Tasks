import csv
import random
import os

lat, long= [],[]

for i in range(100):
    lat.append(round(28.68 +0.01*random.random() , 6))
    long.append(round(77.32 + 0.01 * random.random() , 6))

lat.sort()
long.sort()

filename="route.csv" # relative location that it current dirrectoey


#mode = 'a' if os.path.exists(writepath) else 'w'
if os.path.exists(filename) == False:  
    with open(filename, "w" , newline="") as f:
        wrtr_obj = csv.writer(f) # creating csv writer obj for fileobject f
        for i in range(100):
            loc=(lat[i],long[i]) # tuple of lat and long
            wrtr_obj.writerow(loc)
    print("Done making route.csv, please check it in current directory")

else:
    print("\n\nHehe bouy! it seems you have the file already")
    
