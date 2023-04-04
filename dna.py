#working with fake dna file

import random as r

def evolve(ls):
    p=r.randrange(1,100)
    ind=r.randrange(1,len(ls))
    if p==1:
        if ls[ind]=="0":
            ls[ind]="1"
        else:
            ls[ind]="0"


with open("dna.txt") as f:
    re=f.read()
    lst=list(re)
    print(lst)

for i in range(1,10000):
    evolve(lst)

print(lst)#call by refernce hence changes inlist can be seen in orignal list too
