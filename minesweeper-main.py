#wonderful minesweeper game
#lets begin
#I apologize in advance for the mess I created. I am still shaky with python but at least I could write this!
#When I started writing this I hardly knew how to define a function and read/write to and from files and all that and now I know most of this rather well even if my methods are off.

#import libraries
import random

#global variables
MINIMUM_SIZE = 5
MAXIMUM_SIZE = 10

#define other classes and functions

#save game
def save_game(BOARD, MINES, size):
    try:
        with open("savegame.txt", "w") as save:
            save.write(str(size) + '\n')
            for row in range(size):
                for col in range(size):
                    save.write(str(BOARD[row][col]))
                save.write('\n')
            for row in range(size):
                for col in range(size):
                    save.write(str(MINES[row][col]))
                save.write('\n')
    except:
        print("Could not save game. EXITING...")
        quit()

#load game
def load_game():
    x = -1
    size = 0
    board = []
    mines = []
    #iterate through the file and find pieces needed
    with open("savegame.txt", "r") as load:
        for line in load:
            if x == -1:
                size = int(line)
                x +=1
            elif x < size:
                board.append(list(line.rstrip()))
                x +=1
            else:
                mines.append(list(line.rstrip()))
    return (board, mines, size)



def create_blank_board(size):
    #generate blank board to be used
    blank_board = [['-' for i in range(size)] for i in range(size)]
    return blank_board

#generates random mines
def create_mines(size):
    i = 0
    number_of_mines = size - 1
    temp_board = create_blank_board(size)

    #generate mine board
    while i != number_of_mines:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if temp_board[x][y] != 'X':
            temp_board[x][y] = 'X'
            i += 1
        else:
            continue

    return temp_board

#prints the board
def display_board(BOARD, size):
    toplabel = '  '

    for i in range(size):
        toplabel = toplabel + str(i) + ' '
    print(toplabel)

    i = 0
    for row in BOARD:
        print(i, *row, ' ')
        i += 1

#check for mines next to move
def mine_check(col, row, BOARD, MINES, size):
    mines = 0
    try:
        #check up
        if MINES[row - 1][col] == 'X' and row + 1 > -1:
            mines += 1
        #else:
            #BOARD = place_move(col, row - 1, BOARD, MINES, size)
    except:
        pass
    try:
        #check down
        if MINES[row + 1][col] == 'X' and row + 1 < (size - 1):
            mines += 1
    except:
        pass
    try:
        #check left
        if MINES[row][col - 1] == 'X' and col - 1 > -1:
            mines += 1
    except:
        pass
    try:
        #check right
        if MINES[row][col + 1] == 'X' and col + 1 < (size - 1):
            mines += 1
    except:
        pass
    try:
        #check up right
        if MINES[row - 1][col + 1] == 'X' and (row - 1 > -1 and col + 1 < (size - 1)):
            mines += 1
    except:
        pass
    try:
        #check down right
        if MINES[row + 1][col + 1] == 'X' and (row + 1 < (size - 1) and col + 1 < (size - 1)):
            mines += 1
    except:
        pass
    try:
        #check up left
        if MINES[row - 1][col - 1] == 'X' and (row - 1 > -1 and col - 1 > -1):
            mines += 1
    except:
        pass
    try:
        #check down left
        if MINES[row + 1][col - 1] == 'X' and (row + 1 < (size - 1) and col - 1 > -1):
            mines += 1
    except:
        pass
    return int(mines)

def place_move(col, row, BOARD, MINES, size):
    BOARD[int(row)][int(col)] = mine_check(int(col), int(row), BOARD, MINES, size)
    return BOARD

def not_a_mine(col, row, MINES):
    if MINES[int(row)][int(col)] != 'X':
        return True
    else:
        return False

#returns true if the number of moves the player has made is equal to all possible moves that arent a mine
def game_won_decider(moves, size):
    temp = (size * size) - (size - 1)
    if moves == temp:
        return True
    else:
        return False

#play the game
def play_game(BOARD, MINES, size):
    not_dead = True
    game_won = False
    move_count = 0

    #loop until death or win
    while not_dead and not game_won:
        #option to play, save or quite
        print("Would you like to:")
        print("    Option 1: make a move")
        print("    Option 2: save and quit")
        print("    Option 3: quit without saving")
        print("=================================")
        option = input("Option: ")

        #perform option
        if option == '1':
            pass
        elif option == '2':
            save_game(BOARD, MINES, size)
            quit()
        elif option == '3':
            quit()
        else:
            print("Please choose a valid option")
            continue
        #display board, collect input, and perform operations and checks
        display_board(BOARD, size)
        try:
            col = input("col: ")
            row = input("row: ")
            BOARD = place_move(col, row, BOARD, MINES, size)
            display_board(BOARD, size)
        except:
            print("invalid move")
            continue

        if not not_a_mine(col, row, MINES):
            not_dead = False
        move_count += 1

        if game_won_decider(move_count, size):
            break

    #end game message based on results
    if not_dead:
        print("You Won!")
    else:
        print("You Lost!")
        try:
            x = input("Type anything to exit.")
            quit()
        except:
            quit()



#define the main function
def main():
    #initial prompt
    print("This is a minesweeper game.")
    print("Please follow prompts as to avoid any unnecesarry errors.")
    print("=========================================================")
    print("")

    while True:
        #collect user preference
        print("Would you like to start a new game or load a saved game?")
        print("    Option 1: Start a new game")
        print("    Option 2: Continue a saved game")
        print("========================================================")
        temp = input("Option: ")
        option = int(temp)
        if option == 1 or option == 2:
            break
        else:
            print("Please choose a valid option")
    if option == 1:
        #collect board size
        while True:
            try:
                boardSize = input("What size of board would you like(only size 5-10): ")
                board_size = int(boardSize)
                print("")

                #check for errors
                if board_size < MINIMUM_SIZE or board_size > MAXIMUM_SIZE:
                    print("Please enter a number between 5 and 10.")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a number")

        #pass size to function, generate and display boards before playing game
        BOARD = create_blank_board(board_size)
        MINES = create_mines(board_size)
        display_board(BOARD, board_size)

        #used for checking purposes ive deleted most of my tests but this one i keep using
        #for row in MINES:
            #print(*row, ' ')

        #play game
        play_game(BOARD, MINES, board_size)

    elif option == 2:
        #call loading function
        try:
            BOARD, MINES, board_size = load_game()
        except:
            print("It looks like you don't have a valid save file yet. Please start a new game.")
            print("")
            main()
        #display board before starting game
        display_board(BOARD, board_size)
        #play game
        play_game(BOARD, MINES, board_size)

main()
