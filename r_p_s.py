'''rock paper scissior '''
import getpass

def r_p_s(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3 # if the integer might be like 3,4,5 or 6,7,8 or series continues
    p2=int(num2[bit2])%3 
    '''note that since payer1 and2 are global to the program hecne thy can be accessd in the function without any need to pass them'''
    if player1[p1]==player2[p2]:
        print("Draw")
    elif player1[p1]=="rock" and player2[p2]=="paper":
        print("Player 2 wins")
    elif player1[p1]=="rock" and player2[p2]=="scissor":
        print("Player 1 wins")
    elif player1[p1]=="paper" and player2[p2]=="rock":
        print("Player 1 wins")
    elif player1[p1]=="paper" and player2[p2]=="scissor":
        print("Player 2 wins")
    elif player1[p1]=="scissor" and player2[p2]=="rock":
        print("Player 2 wins")
    elif player1[p1]=="scissor" and player2[p2]=="paper":
        print("Player 1 wins")

player1={0:"rock",1:"paper",2:"scissor"}
player2={1:"rock",0:"paper",2:"scissor"}
while(1):
    num1=input("Player 1 enter your choice : ")
    num2=input("Player 2 enter your choice : ")
    bit1=int(getpass.getpass(prompt="Enter secret bit positon : "))
    bit2=int(getpass.getpass(prompt="Enter secret bit positon : "))
    r_p_s(num1,num2,bit1,bit2)
    ch=input("Do you eant to play again? y/n : ")
    if ch=='n':
        break