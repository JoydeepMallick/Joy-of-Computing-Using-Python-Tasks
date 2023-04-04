from PIL import Image
import random

end=100

def show_board():
	img=Image.open('slb.jpg')
	img.show()

def check_ladder(n):
	ladder={8:26,\
			21:82,\
			50:91,\
			43:77,\
			54:93,\
			66:87,\
			62:96,\
			80:100}
	if n in ladder.keys():
		print("Ladder")
		return(ladder[n])
	else:
		return n


def check_snake(n):
	snake={ 44:19,\
			46:5,\
			48:9,\
			52:11,\
			55:7,\
			59:17,\
			64:36,\
			69:9,\
			73:1,\
			83:19,\
			92:51,\
			95:24,\
			98:28}
	if n in snake.keys():
		print("Snake")
		return(snake[n])
	else:
		return n

def reached_end(point):
	if point==end:
		return True
	else:
		return False

def play():
	p1_name=input("Enter player 1 name : ")
	p2_name=input("Enter player 2 name : ")
	p1,p2=0,0 
	turn=0
	while(1):
		if turn%2==0:
			print(p1_name," your turn")
			c=int(input("Press 1 to continue, 0 to quit : "))
			if c==0:
				print(p1_name," scored ",p1)
				print(p2_name," scored ",p2)
				print("Quitting the game, Thanks for playing")
				break
			dice=random.randint(1,6)
			print("Dice showed: ",dice)
			p1+=dice
			p1=check_ladder(p1)
			p1=check_snake(p1)

			if p1>end:
				p1=end
			print(p1_name," your score ",p1 )
			if reached_end(p1):
				print(p1_name," won")
				break
		else:
			print(p2_name," your turn")
			c=int(input("Press 1 to continue, 0 to quit : "))
			if c==0:
				print(p1_name," scored ",p1)
				print(p2_name," scored ",p2)
				print("Quitting the game, Thanks for playing")
				break
			dice=random.randint(1,6)
			print("Dice showed: ",dice)
			p2+=dice
			p2=check_ladder(p2)
			p2=check_snake(p2)

			if p2>end:
				p2=end
			print(p2_name," your score ",p2 )
			if reached_end(p2):
				print(p2_name," won")
				break

		turn+=1

show_board()
play()