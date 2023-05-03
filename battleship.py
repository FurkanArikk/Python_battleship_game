from random import randint

#Board for ship location
Hidden_Board = [[" "] * 8 for x in range(8)]

# Board that displaying location of our guesses
Guess_Board = [[" "] * 8 for i in range(8)]

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# creating the ships
def create_ships(board):
    for ship in range(4):
        # you can change the number of the ships I created 4 ship
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

def get_ship_location():
    row = input("Please enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Please enter the row of the ship: ").upper()
    column = input("Please enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Please enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count
create_ships(Hidden_Board)
print(Hidden_Board)
print(Guess_Board)

if __name__ == "__main__":
    create_ships(Hidden_Board)
    print(Hidden_Board)
    print(Guess_Board)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        print_board(Guess_Board)
        row, column = get_ship_location()
        if Guess_Board[row][column] == "O":
            print("You already destroyed that ship.")
        elif Hidden_Board[row][column] == "X":
            print("Hit !!")
            Guess_Board[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS !!!")
            Guess_Board[row][column] = "O"   
            turns -= 1     
        if count_hit_ships(Guess_Board) == 4:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")
