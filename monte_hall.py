import random
swap,dont_swap=0,0
i=0
while(i<10):
	doors,goatdoor=[None]*3,[]
	##the aboove counts only when you win

	x=random.randint(0,2)###for actual door
	doors[x]="your reward"##hiding the reward in some random door(different evey time)

	'''please note the list comprehension format of the two lists given below'''
	doors=["goat" if ele==None else ele for ele in doors]
	goatdoor=[i for i in range(3) if doors[i]=="goat"]

	ch_door=int(input("Enter your choice(0,1,2) : "))
	door_open=random.choice(goatdoor)## revealing a door with goat,hence 2 choices left

	while door_open==ch_door:
		##revealed door must not be the choice
		door_open=random.choice(goatdoor)
	'''asking the player if he wants to swap '''
	ch=input("Do you want to swap? y/n : ")
	if ch=='y':
		if doors[ch_door]=="goat":
			# player has swapped so his old choice if goat he wins
			print("You win!!")
			swap+=1
		else:
			print("You lose")
	else:
		if doors[ch_door]=="goat":
			print("You lose")
		else:
			print("You win!!")
			dont_swap+=1

	i+=1

print("Swap",swap)
print("no swapped",dont_swap)
