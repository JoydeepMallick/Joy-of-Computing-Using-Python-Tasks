import random

##old sluggish method hmers big files

movies = open('movies.txt', encoding="utf8").read().split()
''' encoding is provided since it cant understand the given encoding
which might not be the default one which is supported'''

movies=[movie[0:movie.find("(")].lower() for movie in movies]##all names havelower case
rand_mov =random.choice(movies)
try:
	if rand_mov[-1]==":" or rand_mov.find(':')!=-1:##more work needed for nameless movie😯done
		rand_mov=rand_mov[:len(rand_mov)-1]##cleaning movie name
except:
	rand_mov=''#its blank name 

#print(rand_mov,"\n\n")


def create_ques(movie):
	mv_letters=list(movie)
	temp=[]
	for i in mv_letters:
		if i==' ':
			# print(i)
			temp.append(' ')
		else:
			# print(i)
			temp.append('*')
	qn=''.join(str(x) for x in temp)
	# print(temp)
	return qn

def ispresent(letter,movie):##checks if letter is prsent in movie
	c=movie.count(letter)#if frequency of digit is zero not found
	#alternative:-
	#
	#c=movie.find(letter)
	#if c==-1:not found
	#
	if c==0:
		return False
	else:
		return True

def unlock(qn,movie,letter):#since letter is present in movie it places it in the desired postion
	mv_letters,qn_list=list(movie),list(qn)
	temp=[]
	for i in  range(len(mv_letters)):
		if mv_letters[i] in [' ',letter]: ## if postion of movie contains either space or NEW guessed letter keep them at its position
			temp.append(mv_letters[i])
		else:## working with the question part
			if qn_list[i]=='*':
				temp.append('*')
			else:
				temp.append(mv_letters[i])##the already guessed letters appear before
	new_qn=''.join(str(x) for x in temp)
	return new_qn


def play():
	p1=input("Enter player 1 name : ")
	p2=input("Enter player 2 name : ")
	ps1,ps2,turn=0,0,0
	willing=True
	while(willing):
		if turn%2==0:
			#player 1
			print(p1,", your turn")
			rand_mov =random.choice(movies)
			print("\n\n\nMovie nme : ",rand_mov,"(please dont look)😆\n\n\n")##cooment it pls
			qn=create_ques(rand_mov)
			print("\n",qn)
			modified_qn=qn

			not_said=True
			while not_said:
				letter=input("\nYour letter : ")
				if ispresent(letter,rand_mov):
					#unlock
					modified_qn=unlock(modified_qn,rand_mov,letter)
					print("\n",modified_qn)

					d=int(input("\n\npress\n1. to guess movie name\n2.to unlock another letter : "))#after at least one letter is guessed
					if d==1:
						if input("\nEnter movie name : ").lower()==rand_mov.lower():#checking fter ignoreing case
							ps1+=1
							print("True")
							not_said=False##breaks out of while loop
							print(p1," your score is ",ps1)
						else:
							print("Wrong ! try again\n")
				else:
					print(letter," not found!\n")

			c=int(input("\n\n1.to continue\n2,to exit : "))
			if c==2:
				print(p1," scored ",ps1,"\n",p2," scored ",ps2)
				print("Thanks for playing!\n")
				willing=False
			elif c==1:
				willing=True##willing is true till now 
			else:
				print("\nSeems you entered wrong! Continuing game.............\n")
		else:
			
			#player 2 and so on alternately
			print(p2,", your turn")
			rand_mov =random.choice(movies)
			print("\n\n\nMovie nme : ",rand_mov,"(plase dont look😆\n\n\n")##cooment it pls
			qn=create_ques(rand_mov)
			print("\n",qn)
			modified_qn=qn

			not_said=True
			while not_said:
				letter=input("\nYour letter : ")
				if ispresent(letter,rand_mov):
					#unlock
					modified_qn=unlock(modified_qn,rand_mov,letter)
					print("\n",modified_qn)

					d=int(input("press\n1. to guess movie name\n2.to unlock another letter : "))#after at least one letter is guessed
					if d==1:
						if input("\nEnter movie name : ").lower()==rand_mov.lower():#checking fter ignoreing case
							ps2+=1
							print("True")
							not_said=False##breaks out of while loop
							print(p2," your score is ",ps2)
						else:
							print("Wrong ! try again\n")
				else:
					print(letter," not found!\n")

			c=int(input("\n\n1.to continue\n2,to exit : "))
			if c==2:
				print("\n\n",p1," scored ",ps1,"\n",p2," scored ",ps2)
				print("\nThanks for playing!\n")
				willing=False
			elif c==1:
				willing=True##willing is true till now 
			else:
				print("\nSeems you entered wrong! Continuing game.............\n")

		turn+=1##now next player 


print("\nGUESS THE MOVIE GAME\n\n\n")
play()