import numpy as np
import turtle as t
from turtle import *

# initialize random number generator object
rng = np.random

# initialize the previous shot and result for the bot's first turn
previous_shot = [-1, -1]
previous_result = -1

# initialize the game boards and display boards
board1 = np.zeros((6, 6))
blank_board = '+-----------------------------------+\n|  .  |  .  |  .  |  .  |  .  |  .  |\n'
blank_board *= 6
blank_board += '+-----------------------------------+'
display_board1 = blank_board.split(' ')
strategy_board1 = blank_board.split(' ')

board2 = np.zeros((6, 6))
display_board2 = blank_board.split(' ')
strategy_board2 = blank_board.split(' ')

board3 = np.zeros((6, 6))

blank = '\n' * 40

# initialize high score variables
winner = ''
pturn1 = 0
pturn2 = 0
pturn3 = 0

# initialize bot algorithm variables
turn = -1
streak = 0


def carrier(board, display, ship_length):
    """
    This function will place a ship on the player's board
    :param board: which board is being changed, (p1 or p2)
    :param display: which display board is being changed, (p1 or p2)
    :param ship_length: the length of the ship trying to be placed
    :return: none
    """
    while True:
        # print their board
        if display == display_board1:
            print('Player 1\'s board:')
        elif display == display_board2:
            print('Player 2\'s board:')
        print(*display)
        try:
            print('Input the row and column you wish to start your ship of length {}'.format(ship_length))
            # ask for the starting and ending coordinates of their ship
            start = [int(input('Row Start')), int(input('Column Start'))]
            orientation = input('Place ship horizontal or vertical (input h or v)')
            if orientation == 'h':
                end = [start[0], start[1] + ship_length - 1]
            elif orientation == 'v':
                end = [start[0] + ship_length - 1, start[1]]
            else:
                print('Your input was invalid')
                continue
            # check that the inputs are inbounds
            if start[0] < 1 or start[0] > 6 or start[1] < 1 or start[1] > 6:
                print('Your input was invalid')
                continue
            elif end[0] < 1 or end[0] > 6 or end[1] < 1 or end[1] > 6:
                print('Your input was invalid')
                continue

            if boat_check(start, end, board):
                # if the boat is in the same row / column it is vertical or horizontal
                if start[0] == end[0]:  # same row
                    length = np.abs(start[1] - end[1])  # check for the length of the ship
                    if length == ship_length - 1:
                        for i in range(start[1], end[1] + 1):  # if it's valid, fill a ship between the coordinates
                            board[start[0] - 1][i - 1] = 1
                        print('Carrier is set')
                        display_board(board, display)
                        break
                    else:
                        print('Your input was invalid')

                elif start[1] == end[1]:  # repeat above process if the ship is in the same column
                    length = np.abs(start[0] - end[0])
                    if length == ship_length - 1:
                        for i in range(start[0], end[0] + 1):
                            board[i - 1][start[1] - 1] = 1
                        print('Carrier is set')
                        display_board(board, display)
                        break
                    else:
                        print('Your input was invalid')
                else:
                    print('Your input was invalid')
        # if their input is outside the bounds of the board, try again
        except ValueError:
            print('Your input was invalid')
            continue


def bot_generator(board, ship_length):
    """
    This function generates a random board for the bot in single player
    :param board: changes the bots board
    :param ship_length: the length of the ship trying to be placed
    :return: none
    """
    while True:
        try:
            # generate a random start & end for the boat
            start = [rng.randint(1, 7), rng.randint(1, 7)]
            orientation = rng.randint(1, 3)
            if orientation == 1:
                orientation = 'h'
            elif orientation == 2:
                orientation = 'v'

            if orientation == 'h':
                end = [start[0], start[1] + ship_length - 1]
            elif orientation == 'v':
                end = [start[0] + ship_length - 1, start[1]]
            else:
                continue

            # check that the inputs are inbounds
            if start[0] < 1 or start[0] > 6 or start[1] < 1 or start[1] > 6:
                continue
            elif end[0] < 1 or end[0] > 6 or end[1] < 1 or end[1] > 6:
                continue

            if bot_check(start, end, board):
                # if the boat is in the same row / column it is vertical or horizontal
                if start[0] == end[0]:  # same row
                    length = np.abs(start[1] - end[1])  # check for the length of the ship
                    if length == ship_length - 1:
                        for i in range(start[1], end[1] + 1):  # if it's valid, fill a ship between the coordinates
                            board[start[0] - 1][i - 1] = 1
                        break

                elif start[1] == end[1]:  # repeat above process if the ship is in the same column
                    length = np.abs(start[0] - end[0])
                    if length == ship_length - 1:
                        for i in range(start[0], end[0] + 1):
                            board[i - 1][start[1] - 1] = 1
                        break
        # if their input is outside the bounds of the board, try again
        except ValueError:
            continue


def boat_check(start, end, board):
    """
    checks that the boat trying to be placed doesn't overlap existing boats
    :param start: starting coordinate of the boat
    :param end: ending coordinate of the boat
    :param board: which board is being changed
    :return: True or False if boat is valid
    """
    # checks that either the row or column of the start/end are the same
    if start[0] == end[0]:
        for i in range(start[1], end[1] + 1):  # checks that there isn't a 1 in the range of placed ships
            if board[start[0] - 1][i - 1] == 1:
                print('Your input was invalid')
                return False  # returns false, which continues the boat placing function loop
            else:
                continue
    elif start[1] == end[1]:
        for i in range(start[0], end[0] + 1):
            if board[i - 1][start[1] - 1] == 1:
                print('Your input was invalid')
                return False
            else:
                continue
    else:
        print('Your input was invalid')
        return False
    return True  # if the placement passes all the tests, run the boat placing function


def bot_check(start, end, board):
    """
    checks that the boat trying to be placed doesn't overlap existing boats for the bot
    :param start: starting coordinate of the boat
    :param end: ending coordinate of the boat
    :param board: which board is being changed
    :return: True or False if the board is valid or not
    """
    # checks that either the row or column of the start/end are the same
    if start[0] == end[0]:
        for i in range(start[1], end[1] + 1):  # checks that there isn't a 1 in the range of placed ships
            if board[start[0] - 1][i - 1] == 1:
                return False  # returns false, which continues the boat placing function loop
            else:
                continue
    elif start[1] == end[1]:
        for i in range(start[0], end[0] + 1):
            if board[i - 1][start[1] - 1] == 1:
                return False
            else:
                continue
    else:
        return False
    return True  # if the placement passes all the tests, run the boat placing function


def display_board(board, display):
    """
    changes the display board
    :param board: board being changed
    :param display: display board being changed
    :return: none
    """
    for i in range(6):
        for j in range(6):
            if board[i][j] == 1:
                display[2 + j * 4 + i * 24] = 'X'


def player1_boats():
    """
    creates boats for player 1
    :return: none
    """
    carrier(board1, display_board1, 4)
    carrier(board1, display_board1, 3)
    carrier(board1, display_board1, 3)
    carrier(board1, display_board1, 2)


def player2_boats():
    """
    creates boats for player 2
    :return: none
    """
    carrier(board2, display_board2, 4)
    carrier(board2, display_board2, 3)
    carrier(board2, display_board2, 3)
    carrier(board2, display_board2, 2)


def bot_boats():
    """
    creates boats for the bot
    :return: none
    """
    bot_generator(board3, 4)
    bot_generator(board3, 3)
    bot_generator(board3, 3)
    bot_generator(board3, 2)


def player1_turn(board):
    """
    runs through player1's turn
    :param board: which board is being changed
    :return: none
    """
    while True:
        try:
            # display the players boards
            print('Player 1\'s board:\n', *display_board1)
            print('Player 1\'s strategy board\n', *strategy_board1)
            print('Enter the coordinate you wish to shoot')
            shot = [int(input('Row:')) - 1, int(input('Column')) - 1]  # ask for the user's shot
            # check the opponents board, and determine if there is a ship there
            if board[shot[0]][shot[1]] == 0:
                on_miss(shot[0], shot[1], board, display_board2, strategy_board1)
            elif board[shot[0]][shot[1]] == 1:
                on_hit(shot[0], shot[1], board, display_board2, strategy_board1)
            elif board1[shot[0]][shot[1]] == 2:
                print('You already shot this tile')
                continue
            elif board1[shot[0]][shot[1]] == 3:
                print('You already shot this tile')
                continue
        except ValueError:
            print('Your shot was invalid')
            continue
        except IndexError:
            print('Your shot was invalid')
            continue
        break


def player2_turn():
    """
    runs through player 2's turn
    :return: none
    """
    while True:
        try:
            # repeat of above process for player 2
            print('Player 2\'s board:\n', *display_board2)
            print('Player 2\'s strategy board\n', *strategy_board2)
            print('Enter the coordinate you wish to shoot')
            shot = [int(input('Row:')) - 1, int(input('Column')) - 1]
            if board1[shot[0]][shot[1]] == 0:
                on_miss(shot[0], shot[1], board1, display_board1, strategy_board2)
            elif board1[shot[0]][shot[1]] == 1:
                on_hit(shot[0], shot[1], board1, display_board1, strategy_board2)
            elif board1[shot[0]][shot[1]] == 2:
                print('You already shot this tile')
                continue
            elif board1[shot[0]][shot[1]] == 3:
                print('You already shot this tile')
                continue
        except ValueError:
            print('Your shot was invalid')
            continue
        except IndexError:
            print('Your shot was invalid')
            continue
        break


def bot_turn():
    """
    runs through the bots turn
    :return: none
    """
    # initialize global variables for the algorithm
    global turn
    global streak
    global shot_hit
    while True:
        try:
            # generate a shot from the bot_shot() function
            shot = bot_shot()
            # check if there's a ship on the opponents board and write the result to the text file
            if board1[shot[0]][shot[1]] == 0:
                text = open('bot_moves.txt', 'a')
                on_miss(shot[0], shot[1], board1, display_board1, strategy_board2)
                text.write('{},{},2\n'.format(shot[0], shot[1]))
                text.close()
            elif board1[shot[0]][shot[1]] == 1:
                text = open('bot_moves.txt', 'a')
                on_hit(shot[0], shot[1], board1, display_board1, strategy_board2)
                text.write('{},{},3\n'.format(shot[0], shot[1]))
                streak = 1
                shot_hit = turn + 1
                text.close()
            # if the bot already shot the tile, retry until a valid shot is selected
            elif board1[shot[0]][shot[1]] == 2:
                continue
            elif board1[shot[0]][shot[1]] == 3:
                continue
        except ValueError:
            continue
        except IndexError:
            continue
        turn += 1
        break


def bot_shot():
    """
    chooses the bots shot
    :return: none
    """
    # on the first turn, the bot shoots randomly
    # if the bot hits a ship, it will shoot perpendicularly until it hits again, then the counter will reset
    # if the bot shoots perpendicularly and there is no hit, it will return to shooting randomly until a ship is hit
    global streak
    if turn == -1:
        shot = [rng.randint(0, 6), rng.randint(0, 6)]
        return shot
    text = open('bot_moves.txt', 'r')
    shotlist = text.readlines()
    for i in range(len(shotlist)):
        shotlist[i] = shotlist[i][:5]
        shotlist[i] = shotlist[i].split(',')
    text.close()

    if streak == 0:
        shot = [rng.randint(0, 6), rng.randint(0, 6)]
        return shot

    if streak == 1:
        shot = [int(shotlist[shot_hit][0]), int(shotlist[shot_hit][1])]
        if shot[0] == 0:
            streak += 1
        else:
            shot[0] -= 1
            streak += 1
            return shot

    if streak == 2:
        shot = [int(shotlist[shot_hit][0]), int(shotlist[shot_hit][1])]
        if shot[1] == 5:
            streak += 1
        else:
            shot[1] += 1
            streak += 1
            return shot

    if streak == 3:
        shot = [int(shotlist[shot_hit][0]), int(shotlist[shot_hit][1])]
        if shot[0] == 5:
            streak += 1
        else:
            shot[0] += 1
            streak += 1
            return shot

    if streak == 4:
        shot = [int(shotlist[shot_hit][0]), int(shotlist[shot_hit][1])]
        if shot[1] == 0:
            streak += 1
        else:
            shot[0] -= 1
            streak += 1
            return shot

    streak = 0

    shot = [rng.randint(0, 6), rng.randint(0, 6)]
    return shot


def on_miss(row, column, board, display, strategy):
    """
    changes the board if their shot missed
    :param row: row of missed shot
    :param column: column of missed shot
    :param board: board being changed
    :param display: display being changed
    :param strategy: strategy board being changed
    :return: none
    """
    # changes the game board and display board on a miss
    print(blank)
    print('Your shot missed')
    board[row][column] = 2
    display[2 + column * 4 + row * 24] = 'M'
    strategy[2 + column * 4 + row * 24] = 'M'


def on_hit(row, column, board, display, strategy):
    """
    changes the board if their shot hit
    :param row: row of shot
    :param column: column of shot
    :param board: board being changed
    :param display: display being changed
    :param strategy: strategy board being changed
    :return: none
    """
    # changes the game board and display board on a hit
    print(blank)
    print('Your shot hit!')
    board[row][column] = 3
    display[2 + column * 4 + row * 24] = 'H'
    strategy[2 + column * 4 + row * 24] = 'H'


def multiplayer():
    """
    runs the game in multiplayer mode
    :return: none
    """
    # initialize global variables
    global pturn1
    global pturn2
    global winner
    # create boards for players 1 and 2
    player1_boats()
    print(blank)
    input('Enter space for the next turn')
    player2_boats()
    print(blank)
    input('Enter space for the next turn')
    # alternate between turns until there is a winner
    while True:
        player1_turn(board2)
        pturn1 += 1
        if 1 not in board2:
            winner = 'P1'
            print('Player 1 wins in {} turns!'.format(pturn1))
            break
        input('Enter space for the next turn')
        player2_turn()
        pturn2 += 1
        if 1 not in board1:
            winner = 'P2'
            print('Player 2 wins in {} turns!'.format(pturn2))
            break
        input('Enter space for the next turn')


def single_player():
    """
    runs the game in single player mode
    :return: none
    """
    # same process as multiplayer, but replaces player 2 with the bot
    global pturn1
    global pturn3
    global winner
    with open('bot_moves.txt', 'w') as text:
        text.truncate()
    player1_boats()
    print(blank)
    input('Enter space for the next turn')
    bot_boats()
    print('Bot\'s boats are generated.')
    input('Enter space for the next turn')
    while True:
        player1_turn(board3)
        pturn1 += 1
        if 1 not in board3:
            winner = 'P1'
            print('Player 1 wins in {} turns!'.format(pturn1))
            break
        input('Enter space for the next turn')
        bot_turn()
        pturn3 += 1
        if 1 not in board1:
            winner = 'P3'
            print('Bot wins in {} turns!'.format(pturn3))
            break
        input('Enter space for the next turn')


def instructions():
    """
    Displays the rules of the game
    :return:
    """
    t.title('Battleship Rules')

    t.speed(0)

    t.screensize(canvwidth=0, canvheight=10, bg='white')
    t.width(1)
    t.hideturtle()
    t.penup()
    t.setposition(-400, -150)
    t.color('black')
    t.write(
        'Привет Welcome to Battleship! \nYour objective is to destroy all 4 of your opponents ships before they do.'
        '\nThe ships consist of:\nAircraft Carrier with length of 4\nDestroyer with a length of 3'
        '\nDestroyer with a length of 3\nPatrol Boat with a length of 2 '
        '\n\n\n\n\n\n\n\nRules for Battleship:\nInput whether you want to play against another person or against the '
        'computer \nEnter your coordinates for all 4 of your battleships\n(row and column)\nIf opponent is another '
        'person, they will enter their coordinates next\nIf opponent is AI, coordinates will be randomly chosen\nAfter '
        'you and your opponent place the ships, \nyou will be prompted to enter a row and column as your first shot'
        '\nYou will continue to shoot back and forth until either \nyour or your opponents ships are all sunk.',
        font=('Verdana', 14, 'normal'))

    t.penup()

    t.done()


instructions()

# display the all-time high score
with open('records.txt', 'r') as text:
    print('\nThe high score is {} moves'.format(text.readline()))

# ask the user for single player or multiplayer and run the corresponding function
mode = int(input('\nEnter 1 for single-player, 2 for multi-player'))

if mode == 1:
    single_player()
elif mode == 2:
    multiplayer()
else:
    print('Invalid input, run again')

# check if there is a new high score, if there is, display it and replace it in the text file
with open('records.txt', 'r+') as text:
    high_score = int(text.readline())
    if winner == 'P1':
        if pturn1 < high_score:
            print('New high score! {} moves'.format(high_score))
            text.write(str(high_score))
        elif pturn2 < high_score:
            print('New high score! {} moves'.format(high_score))
            text.write(str(high_score))
        elif pturn3 < high_score:
            print('New high score! {} moves'.format(high_score))
            text.write(str(high_score))
