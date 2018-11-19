import random

def print_board(board):
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|' ,board[8])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('What letter is player 1 (X or O)?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move - 1] = letter

def isWinner(board, letter):
    return ((board[0] == letter and board[1] == letter and board[2] == letter) or #Across the top
            (board[3] == letter and board[4] == letter and board[5] == letter) or #Across the middle
            (board[6] == letter and board[7] == letter and board[8] == letter) or #Across the bottom
            (board[6] == letter and board[3] == letter and board[0] == letter) or #Vertically left side
            (board[7] == letter and board[4] == letter and board[1] == letter) or #Vertically middle
            (board[8] == letter and board[5] == letter and board[2] == letter) or #Vertically right side
            (board[6] == letter and board[4] == letter and board[2] == letter) or #Diagonally
            (board[8] == letter and board[4] == letter and board[0] == letter)) #Diagonally

def isSpaceFree(board, move):
    return board[move - 1] == ' '

def getPlayerMove(board, turn):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move, ' + turn + '? (1-9)')
        move = input()
    return int(move)

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' '] * 10
    playerLetter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Player 1':
            print_board(theBoard)
            move = getPlayerMove(theBoard, turn)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                print_board(theBoard)
                print('Player 1 wins!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'
        else:
            print_board(theBoard)
            move = getPlayerMove(theBoard, turn)
            makeMove(theBoard, player2Letter, move)
            if isWinner(theBoard, player2Letter):
                print_board(theBoard)
                print('Player 2 wins!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not playAgain():
        break
