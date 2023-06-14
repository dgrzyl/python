# Tictactoe game for 2 players by dgrzyl

import time as ti

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]
current_player = 'X'
winner = None
current_player_name = None
gameRunning = True 

def printboard(board):
    print('',board[0][0], '|', board[0][1], '|', board[0][2],)
    for i in range(1,3):
        print(11*'-')
        print('',board[i][0], '|', board[i][1], '|', board[i][2],)
        
#
def playerinput(board):
    while True:
        row = int(input(f'{current_player_name}\'s turn. Write row number where you want to put \'{current_player}\'.\n'
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
            gameRunning = False
            printboard(board)
            print(f'The winner is {current_player_name}!')
        if board[0][i] == board[1][i] == board[2][i] != ' ':    #checking cols
            winner = current_player
            gameRunning = False
            printboard(board)
            print(f'The winner is {current_player_name}!')
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = current_player
        gameRunning = False
        printboard(board)
        print(f'The winner is {current_player_name}!')
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = current_player
        gameRunning = False
        printboard(board)
        print(f'The winner is {current_player_name}!')

#checking for tie
def checktie(board):
    global gameRunning
    if ' ' not in [spot for row in board for spot in row]:
        printboard(board)
        print('It\'s a tie! Nobody wins.')
        gameRunning = False

#switching player
def switchPlayer():    
    global current_player
    global current_player_name
    if current_player == 'X':
        current_player = 'O'
        current_player_name = player2_name
    else:
        current_player = 'X'
        current_player_name = player1_name


def getName_1():
    while True:
        player1_name = input('Player 1 name: ')

        if player1_name.strip() != '':
            break
        
        if player1_name.strip() == '':
            print("Player name cannot be empty!\n")

    return player1_name

def getName_2():
    while True:
        player2_name = input('Player 2 name: ')

        if player2_name.strip() != '':
            break
        
        if player2_name.strip() == '':
            print("Player name cannot be empty!\n")

    return player2_name


# Running game
print('Welcome to a TicTacToe game by dgrzyl!')
print(40*'*')
ti.sleep(2)
player1_name = getName_1()
ti.sleep(1)
player2_name = getName_2()
ti.sleep(2)
current_player_name = player1_name
while gameRunning:
    printboard(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    switchPlayer()
    ti.sleep(0.5)
