import random
import matplotlib.pyplot as plt

global account
account=0
x,y=[],[]

def lottery():
    ##bet=int(input("ENter  your bet : "))
    global account
    bet=random.randint(1,10)
##    print("Your bet : ",bet)
    lucky_draw=random.randint(1,10)
##    print("Draw out number is ",lucky_draw)
    if bet==lucky_draw :account+=900-100
    else :account=account-100

##    print("Money in your account :",account)
##    print()

for i in range(int(input("How many das you played ? "))):
    lottery()
    x.append(i+1)
    y.append(account)

print("Money in your account after all the bets :",account)
plt.plot(x,y)
plt.show()
'''
loss is more evident over long play and a sharp fAall in grph curve is seen most of the times so more we play more we loose.
'''
