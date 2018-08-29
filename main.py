
# Udemy Complete Python Bootcamp Project 1

import random

mboard = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

gboard = ["#", "", "", "", "", "", "", "", "", ""]

p1wincount = []
p2wincount = []

def draw_board():
    print('\n'*100)
    # Print both gameboard and move selection board
    print("{:>20}".format("Available Moves") + "{:>27}".format("Game Board"))
    print('\n')
    print('{:>10}'.format(mboard[7]) + "{:<2}".format('|'), end="")
    print('{:<2}'.format(mboard[8]) + "{:<2}".format('|'), end="")
    print('{:<2}'.format(mboard[9]), end="")
    print('{:>20}'.format(gboard[7]) + "{:>2}".format('|'), end="")
    print('{:>2}'.format(gboard[8]) + "{:>2}".format('|'), end="")
    print('{:>2}'.format(gboard[9]))
    print('{:>10}'.format(mboard[4]) + "{:<2}".format('|'), end="")
    print('{:<2}'.format(mboard[5]) + "{:<2}".format('|'), end="")
    print('{:<2}'.format(mboard[6]), end="")
    print('{:>20}'.format(gboard[4]) + "{:>2}".format('|'), end="")
    print('{:>2}'.format(gboard[5]) + "{:>2}".format('|'), end="")
    print('{:>2}'.format(gboard[6]))
    print('{:>10}'.format(mboard[1]) + "{:<2}".format('|'), end="")
    print('{:<2}'.format(mboard[2]) + "{:<2}".format('|'), end="")
    print('{:<2}'.format(mboard[3]), end="")
    print('{:>20}'.format(gboard[1]) + "{:>2}".format('|'), end="")
    print('{:>2}'.format(gboard[2]) + "{:>2}".format('|'), end="")
    print('{:>2}'.format(gboard[3]))
    print('\n'*4)

# Player X or O selection


def player_select():
    marker_select = ''

    while not (marker_select == 'X' or marker_select == 'O'):
        marker_select = input("Player 1: Select X or O    ").upper()
    if marker_select == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_mark(gboard, mboard, marker, position):
    gboard[position] = marker
    mboard[position] = ''


def draw_check(mboard):
    counter = 0
    for i in mboard:
        if i == '':
            counter += 1
    if counter >= 9:
        print("Tie Game!")
        return True


def space_check(gboard, position):

    return gboard[position] == ""



def player_choice(gboard, turn):

    position = 0

    while position not in range(1,10) or not space_check(gboard, position):
        position = int(input("{turn}".format(turn = turn) + ": Select a move:  "))

    return position

def win_check(gboard, marker):
    return ((gboard[7] == marker and gboard[8] == marker and gboard[9] == marker) or #top row
    (gboard[4] == marker and gboard[5] == marker and gboard[6] == marker) or         #middle horizontal row
    (gboard[1] == marker and gboard[2] == marker and gboard[3] == marker) or         #bottom row
    (gboard[7] == marker and gboard[4] == marker and gboard[1] == marker) or         #left row
    (gboard[8] == marker and gboard[5] == marker and gboard[2] == marker) or         #middle vertical row
    (gboard[9] == marker and gboard[6] == marker and gboard[3] == marker) or         #right row
    (gboard[7] == marker and gboard[5] == marker and gboard[3] == marker) or         #diagonal 1
    (gboard[9] == marker and gboard[5] == marker and gboard[1] == marker))           #diagonal

def board_reset():
    global mboard
    global gboard
    mboard = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    gboard = ["#", "", "", "", "", "", "", "", "", ""]

def turn_order():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def main_game():
    player1, player2 = player_select()
    turn = turn_order()
    draw_board()
    print(turn + ' will go first.')
    run_trigger = True
    while run_trigger:
        if turn == "Player 1":
            position = player_choice(gboard, turn)
            place_mark(gboard, mboard, player1, position)
            draw_board()
            if win_check(gboard, player1) is True:
                print("Player 1 wins!")
                p1wincount.append(1)
                run_trigger = False
                break
            if draw_check(gboard) is True:
                run_trigger = False
                break
            if win_check(gboard, player2) is True:
                print("Player 2 wins!")
                p2wincount.append(1)
                run_trigger = False
                break
            if draw_check(gboard) is True:
                run_trigger = False
                break
            else:
                turn = "Player 2"
        else:
            position = player_choice(gboard, turn)
            place_mark(gboard, mboard, player2, position)
            draw_board()
            if win_check(gboard, player1) is True:
                print("Player 1 wins!")
                p1wincount.append(1)
                run_trigger = False
                break
            if draw_check(gboard) is True:
                    run_trigger = False
                    break
            if win_check(gboard, player2) is True:
                print("Player 2 wins!")
                p2wincount.append(1)
                run_trigger = False
                break
            if draw_check(gboard) is True:
                run_trigger = False
                break
            else:
                turn = "Player 1"

    while not run_trigger:
        print("Total Score Player 1: {p1} | Player 2: {p2}".format(p1 = sum(p1wincount), p2 = sum(p2wincount)))
        new_game_select = input("Play again? Yes or No?"  ).upper()
        if new_game_select == "Yes".upper():
            board_reset()
            main_game()
        else:
            exit()





main_game()
