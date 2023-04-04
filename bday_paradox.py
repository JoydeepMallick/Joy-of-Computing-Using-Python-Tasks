import math
import random
import datetime

def leap(year):
	if (year%4==0 and year%100!=0) or (year%400==0): return True
	else: return False


def random_day_generator(y,m):
	if leap(y) and m==2:# leap and feb
		d=random.randint(1,29)
	elif leap(y)==False and m==2: # not leap and feb
		d=random.randint(1,28)
	elif m in [1,3,5,7,8,10,12]: # months with 31 days
		d=random.randint(1,31)
	else:
		d=random.randint(1,30)
	return d






bday=[]
i=0
while(i<50):
	year=random.randint(1893,2017)
	# the oldest lived person was 124 years old so 124 consequent years of dob would be good
	month=random.randint(1,12)
	day=random_day_generator(year,month)
	dd=datetime.date(year,month,day)
	day_of_year=dd.timetuple().tm_yday
	bday.append(day_of_year)
	i+=1
bday.sort()
i=0
while(i<50):
	print(bday[i])
	i=i+1

