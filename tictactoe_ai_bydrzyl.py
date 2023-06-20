
# Tictactoe game vs AI by dgrzyl

import time as ti
import random

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]
current_player = 'X'
winner = None
player_name = None
gameRunning = True 

def printboard(board):
    print('',board[0][0], '|', board[0][1], '|', board[0][2],)
    for i in range(1,3):
        print(11*'-')
        print('',board[i][0], '|', board[i][1], '|', board[i][2],)
        
#
def playerinput(board):
    while True:
        row = int(input(f'{player_name}\'s turn. Write row number where you want to put \'{current_player}\'.\n'
                        '1 - first row | 2 - second row | 3 - third row. >> '
                        ))
        col = int(input(f'Write column number where you want to put \'{current_player}\'.\n'
                        '1 - first column | 2 - second column | 3 - third column. >> '
                        ))
        if board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = current_player
            break
        else: 
            print('This spot is already taken! Choose another')
            continue

#checking for winner
def checkwin(board):
    global winner
    global gameRunning
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':    #checking rows
            winner = current_player
            printboard(board)
            print(10*'#',f'The winner is {current_player_name}!',10*'#')
            gameRunning = False
        if board[0][i] == board[1][i] == board[2][i] != ' ':    #checking cols
            winner = current_player
            printboard(board)
            print(10*'#',f'The winner is {current_player_name}!',10*'#')
            gameRunning = False
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = current_player
        printboard(board)
        print(10*'#',f'The winner is {current_player_name}!',10*'#')
        gameRunning = False
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = current_player
        printboard(board)
        print(10*'#',f'The winner is {current_player_name}!',10*'#')
        gameRunning = False

#checking for tie
def checktie(board):
    global gameRunning
    if ' ' not in [spot for row in board for spot in row]:
        printboard(board)
        print(10*'#','It\'s a tie! Nobody wins.',10*'#')
        gameRunning = False

#switching player
def switchPlayer():    
    global current_player
    global current_player_name
    if current_player == 'X':
        current_player = 'O'
        current_player_name = 'AI'
    else:
        current_player = 'X'
        current_player_name = player_name

#AILOGIC

def ai_logic(board):
    flag = True
    while flag:
        #Attacking

        #row check
        for i in range(3):  
            if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == ' ':
                board[i][2] = current_player
                flag = False
        if flag == False:
            break

        for i in range(3):
            if board[i][0] == ' ' and board[i][1] == 'O' and board[i][2] == 'O':
                board[i][0] = current_player
                flag = False
        if flag == False:
            break

        for i in range(3):
            if board[i][0] == 'O' and board[i][1] == ' ' and board[i][2] == 'O':
                board[i][1] = current_player
                flag = False
        if flag == False:
            break
                
        
        #col check
        for i in range(3):  
            if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == ' ':
                board[2][i] = current_player
                flag = False
        if flag == False:
            break
                
        for i in range(3): 
            if board[0][i] == ' ' and board[1][i] == 'O' and board[2][i] == 'O':
                board[0][i] = current_player
                flag = False
        if flag == False:
            break
                
        for i in range(3): 
            if board[0][i] == 'O' and board[1][i] == ' ' and board[2][i] == 'O':
                board[1][i] = current_player
                flag = False
        if flag == False:
            break
                


        #diag check
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == ' ':
            board[2][2] = current_player
            break
        if board[0][0] == ' ' and board[1][1] == 'O' and board[2][2] == 'O':
            board[0][0] = current_player
            break
        if board[0][0] == 'O' and board[1][1] == ' ' and board[2][2] == 'O':
            board[1][1] = current_player
            break

        if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == ' ':
            board[2][0] = current_player
            break
        if board[0][2] == ' ' and board[1][1] == 'O' and board[2][0] == 'O':
            board[0][2] = current_player
            break
        if board[0][2] == 'O' and board[1][1] == ' ' and board[2][0] == 'O':
            board[1][1] = current_player
            break

        #Defence

        #row check
        for i in range(3):  
            if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == ' ':
                board[i][2] = current_player
                flag = False
        if flag == False:
            break
                
        for i in range(3):
            if board[i][0] == ' ' and board[i][1] == 'X' and board[i][2] == 'X':
                board[i][0] = current_player
                flag = False
        if flag == False:
            break
                
        for i in range(3):
            if board[i][0] == 'X' and board[i][1] == ' ' and board[i][2] == 'X':
                board[i][1] = current_player
                flag = False
        if flag == False:
            break
                
        
        #col check
        for i in range(3):  
            if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == ' ':
                board[2][i] = current_player
                flag = False
        if flag == False:
            break
                
        for i in range(3): 
            if board[0][i] == ' ' and board[1][i] == 'X' and board[2][i] == 'X':
                board[0][i] = current_player
                flag = False
        if flag == False:
            break
                
        for i in range(3): 
            if board[0][i] == 'X' and board[1][i] == ' ' and board[2][i] == 'X':
                board[1][i] = current_player
                flag = False
        if flag == False:
            break
                

        #diag check
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == ' ':
            board[2][2] = current_player
            break
        if board[0][0] == ' ' and board[1][1] == 'X' and board[2][2] == 'X':
            board[0][0] = current_player
            break
        if board[0][0] == 'X' and board[1][1] == ' ' and board[2][2] == 'X':
            board[1][1] = current_player
            break

        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == ' ':
            board[2][0] = current_player
            break
        if board[0][2] == ' ' and board[1][1] == 'X' and board[2][0] == 'X':
            board[0][2] = current_player
            break
        if board[0][2] == 'X' and board[1][1] == ' ' and board[2][0] == 'X':
            board[1][1] = current_player
            break
        
        #Starting
        row_val = random.randint(0,2)
        col_val = random.randint(0,2)
        if board[row_val][col_val] == ' ' and flag == True:
            board[row_val][col_val] = current_player
            break

def getName():
    while True:
        player_name = input('Player name: ')

        if player_name.strip() != '':
            break
        
        if player_name.strip() == '':
            print("Player name cannot be empty!\n")

    return player_name

# Running game
print('Welcome to a TicTacToe vs AI game by dgrzyl!')
print(40*'*')
ti.sleep(1)
player_name = getName()
print(40*'*')
ti.sleep(2)

while gameRunning:
    printboard(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    switchPlayer()

    if gameRunning:
        printboard(board)
        ti.sleep(0.5)
        print(40*'*')
        print(15*' '+'AI TURN...')
        print(40*'*')
        ti.sleep(1)
        ai_logic(board)
        checkwin(board)
        checktie(board)
        switchPlayer()
        ti.sleep(0.5)
    else:
        break         
