import math,random,string

symbol=list(string.ascii_letters)
card1,card2=[0]*5,[0]*5   # 5 letter combintions considered

pos1,pos2=random.randrange(0,5),random.randrange(0,5)
#above guesses numers from 0 to 4 ommiting 5

common=random.choice(symbol)#the common symbol to be inserted
symbol.remove(common)#removing already used symbol from list

if pos1==pos2:
	card2[pos1],card1[pos1]=common,common

else:
	card1[pos1],card2[pos2]=common,common
	card1[pos2]=random.choice(symbol)
	symbol.remove(card1[pos2])
	card2[pos1]=random.choice(symbol)
	symbol.remove(card2[pos1])


i=0
while i<5:
	if i!=pos1 and i!=pos2:  #skipping the common  element postion
		other1=random.choice(symbol)
		symbol.remove(other1)
		card1[i]=other1
		other2=random.choice(symbol)
		symbol.remove(other2)
		card2[i]=other2
	i+=1

print(card1,"\n\n",card2)

ch=input("\nEnter the common letter (mind the case): ")
# from threading import Timer

# timeout = 10
# t = Timer(timeout, print, ['Sorry, times up'])
# t.start()
# prompt = "You have %d seconds to choose the correct answer...\n" % timeout
# ch = input("\nEnter the common letter (mind the case): ")
# t.cancel()

if ch==common:
	print("\n\nGood guess buddy!")
else:
	print("\n\nSorry you are a noob!!!")


