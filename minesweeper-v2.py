#this is a revamped version of the origional project written from scratch and incoperating some functions from the origional project
#import board class
from Board_class import *

#define function for reading from file
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

#define size contraints
MINIMUM_SIZE = 5
MAXIMUM_SIZE = 10

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
        option = input("Option: ")

        #if valid option continue the program
        if option == "1" or option == "2":
            break
        else:
            print("Please choose a valid option")

    if option == "1":
        #collect board size
        while True:
            try:
                boardSize = input("What size of board would you like(only size 5-10): ")
                boardSize = int(boardSize)
                print("")

                #check for errors
                if boardSize < MINIMUM_SIZE or boardSize > MAXIMUM_SIZE:
                    print("Please enter a number between 5 and 10.")
                    continue
                else:
                    break
            except:
                print("Please enter a number")
                print("")

        board = Board(boardSize)
        board.play_game()
    elif option == "2":
        try:
            board, mines, size = read_from_file()
            board = Board(size, board, mines, option)
        except:
            print("It appears that you do not have a valid save file.")
            print("Please start a new game to play.")
            print("")

            #call main again to play the game
            main()

#run game
main()
