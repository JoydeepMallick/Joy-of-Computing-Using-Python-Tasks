import numpy
p1s,p2s="X","O"
lst=[["-"]*3]*3
board=numpy.array(lst)

def check_rows(symbol):
    for i in board:
        #print("HEll ",list(i))
        if list(i)==([symbol]*3):  # if row equals ['X','X','X'] if symbol is 'X' and so on
            #print(symbol," won")
            return True 
    return False

def check_cols(symbol):
    for r in range(3):
        count=0
        for c in range(3):  # if col equals ['X','X','X'] if symbol is 'X' and so on
            if board[c][r]==symbol:
                count+=1
        if count==3:
            #print(symbol," won")
            return True 
    return False

def check_diagonals(symbol):
    l_diag=[board[i][i] for i in range(3)]
    r_diag=[board[i][3-i-1] for i in range(3)]
    #print(l_diag,r_diag)
    if [symbol]*3 in [l_diag,r_diag]:
        #print(symbol," won")
        return True 
    return False

def won(symbol):
    #print("row ",check_rows(symbol)," col ",check_cols(symbol)," diag ",check_diagonals(symbol))
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row - 1 ,2 ,3 : "))
        col=int(input("Enter column - 1 ,2 ,3 : "))
        if row in [1,2,3] and col in [1,2,3] and board[row-1][col-1]=="-":
            break 
            # 3 cases checked whether row and colum are valid and the specified cell is vacant
        else:
            print("Seems either the cell doesn't exist or the cell is filled\nPlease try again with some other entry.\n")
    board[row-1][col-1]=symbol
        

def play():
    for turn in range(9): # 9 cells so 9 turns
        if turn% 2==0:
            print("\n X turn :-\n")
            place(p1s)
            if won(p1s) and turn>=4: # at least 5 attempts(3 from X 2 from O) is required to win
                print(numpy.matrix(board))
                print("X won!!!")
                break
        else:
            print("\n O turn :-\n")
            place(p2s)
            if won(p2s) and turn>=5: # at least 6 attempts(3 from O 3 from X) is required to win since X gets first chance
                print(numpy.matrix(board))
                print("O won!!!")
                break
    if not(won(p1s)) and not(won(p2s)): # if no one wins
        print(numpy.matrix(board))
        print("Draw")

play()