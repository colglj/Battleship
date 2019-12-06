"""def generate_board(width=10, height=10):###
generate_board generates a battleship gameboard
determined by the widths and heights of this function
:param width: battleship gameboard width as an int
:param height: battleship gameboard height as an int
:return: returns a battleship gameboard with a list of lists"""

"""for random import randint"""

from typing import List

board = []
	
for x in range(0,5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print (" ".join (row))

print_board(board)

#defining where the ship is
def put_row(board: List) -> int:
    return (2)

def put_col(board):
    return (3) 

"""def put_row(board):
       return randint(0, len(x) - 1)

def put_col(board):
    return randint(0, len(x[0]) - 1)"""


ship_row = put_row(board)
ship_col = put_col(board)

"""show where ship is
print(ship_row)
print(ship_col)"""

#Loop code
for turn in range(4):
    print ("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))


    ##if hit battleship
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations, you sunk my battleship!")
        break
    else:
    #if missed the board
        if guess_row > 5 or guess_col > 5:
            print ("That's not even on the board")
    #if guessed already
        elif board[guess_row][guess_col] == 'X':
            print ("You guessed that already")
    #missed battleship
        else:
            print ("You missed my battleship")
            board[guess_row][guess_col] = 'X'
            if turn == 3:
                print ("Game over")
    print_board(board)



"""
#this is always last line#
if __name__ == '__main__':
	board = generate_board(width=10, height=10)
	print_board(board)"""

