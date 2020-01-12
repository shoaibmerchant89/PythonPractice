import random


def display_board(board):

    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Do you want to be X or O? : ').upper()

    if marker == 'X':
        return ('X','O')
    if marker == 'O':
        return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,marker):
    return (
            (board[7] == marker and board[8] == marker and board[9] == marker) or # top
            (board[4] == marker and board[5] == marker and board[6] == marker) or # middle
            (board[1] == marker and board[2] == marker and board[3] == marker) or # bottom
            (board[7] == marker and board[4] == marker and board[1] == marker) or # left
            (board[8] == marker and board[5] == marker and board[2] == marker) or # center
            (board[9] == marker and board[6] == marker and board[3] == marker) or # right
            (board[7] == marker and board[5] == marker and board[3] == marker) or # diag left to right
            (board[9] == marker and board[5] == marker and board[1] == marker) # diag right to left
    )

def choose_first():
    first = random.randint(1,2)
    if first == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
        return board[position] == ' '
# return True if board[position] is empty

def full_board_check(board):
    for i in range(1,9):
        if space_check(board,i):
            return False
    return True
# If space_check returns empty, then Return False and stop the loop - board is not full
# If space_check returns value for the complete iteration, then Return True - board is full


def player_choice(board,player):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(player + ' - Choose your next position: (1-9)'))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Are you ready to go first? Enter Yes or No: ').lower()

    if play_game.startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard,'Player 1')
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Player 1 wins!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard,'Player 2')
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break