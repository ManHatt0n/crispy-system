board = [["+-------+-------+-------+\n"]
        ,['|', ' '*5, '|', ' '*5, '|', ' '*5, '|\n']
        ,['|  ', '1', '  |  ', '2','  |  ', '3', '  |\n']
        ,['|', ' '*5, '|', ' '*5, '|', ' '*5, '|\n']
        ,["+-------+-------+-------+\n"]
        ,['|', ' '*5, '|', ' '*5, '|', ' '*5, '|\n']
        ,['|  ', '4', '  |  ', "X",'  |  ', '6', '  |\n']
        ,['|', ' '*5, '|', ' '*5, '|', ' '*5, '|\n']
        ,["+-------+-------+-------+\n"]
        ,['|', ' '*5, '|', ' '*5, '|', ' '*5, '|\n']
        ,['|  ', '7', '  |  ','8','  |  ','9', '  |\n']
        ,['|', ' '*5, '|', ' '*5, '|', ' '*5, '|\n']
        ,["+-------+-------+-------+\n"]]

def DisplayBoard(board):
    for row in board:
        for item in row:
            print(item, end =' ')
        print()
          
DisplayBoard(board)

#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#



def EnterMove():
    global board
    while True:
        player_move = int(input("Enter your move: ", ))
        if player_move <= 0 or player_move >= 9:
            print('Not a valid move')
            continue
        #elif [[(str(player_move) != item) for item in row] for row in board]:
         #   print('Not a valid move')
          #  continue
        else:
            board = [[item.replace((str(player_move)), 'O') for item in row] for row in board]
        
        break
        return DisplayBoard(board)           
                
EnterMove()


#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#


def MakeListOfFreeFields(board):
    global free_square
    free_square = []  
    for row in board:
        for item in row:
            if item == '1':
                free_square.append(item)
                
            elif item == '2':
                free_square.append(item)
            
            elif item == '3':
                free_square.append(item)
                
            elif item == '4':
                free_square.append(item)
                
            elif item == '6':
                free_square.append(item)
                
            elif item == '7':
                free_square.append(item)
                
            elif item == '8':
                free_square.append(item)
                
            elif item == '9':
                free_square.append(item)
                

    #print(free_square)
                

MakeListOfFreeFields(board)

#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
sign = 'You won!'

def VictoryFor(board, sign):
    if board[2][1] == 'X' and board[2][3] == 'X' and board[2][5] == 'X': #horiz top X
        return print(sign)
    elif board[2][1] == 'O' and board[2][3] == 'O' and board[2][5] == 'O': #horiz top O
        return print(sign)
    elif board[6][1] == 'X' and board[6][3] == 'X' and board[6][5] == 'X':#horiz mid X
        return print(sign)
    elif board[10][1] == 'X' and board[10][3] == 'X' and board[10][5] == 'X': #horiz bottom X
        return print(sign)
    elif board[10][1] == 'O' and board[10][3] == 'O' and board[10][5] == 'O': #horiz bottom O
        return print(sign)
    elif board[2][1] == 'X' and board[6][3] == 'X' and board[10][5] == 'X': #diag tl to br X
        return print(sign)
    elif board[2][5] == 'X' and board[6][3] == 'X' and board[10][1] == 'X': #diag tr to bl X
        return print(sign)
    elif board[2][1] == 'O' and board[6][1] == 'O' and board[10][1] == 'O': #vert left O
        return print(sign)
    elif board[2][1] == 'X' and board[6][1] == 'X' and board[10][1] == 'X': #vert left X
        return print(sign)
    elif board[2][5] == 'O' and board[6][5] == 'O' and board[10][5] == 'O': #vert right O
        return print(sign)
    elif board[2][5] == 'X' and board[6][5] == 'X' and board[10][5] == 'X': #vert right X
        return print(sign)
    elif board[2][3] == 'X' and board[6][3] == 'X' and board[10][3] == 'X': #vert mid X
        return print(sign)
    
VictoryFor(board, sign)

#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove():
    global board
    from random import choice
    for i in range(0, 1):
        comp_move = choice(free_square)
        #print(comp_move)
        board = [[item.replace((str(comp_move)), 'X') for item in row] for row in board]
        return DisplayBoard(board)
    
DrawMove()


def RepeatFunc():
    EnterMove()
    MakeListOfFreeFields(board)
    VictoryFor(board, sign)
    DrawMove()
    global free_square
    free_square = []
    RepeatFunc()

RepeatFunc()
#
# the function draws the computer's move and updates the board
#
