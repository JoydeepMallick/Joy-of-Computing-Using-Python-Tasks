import math
import random
import string
import os
import time
import sys
import metrics

#import pickle
#import numpy
#import pandas
#import sklearn
#import matplotlib


for i in range(int(input())):
	x1,x2,y1,y2=map(int, input().split())

	if x1/y1 > x2/y2:
		print(-1)
	elif x1/y1 == x2/y2:
		print(0)
	else:
		print(1)
	