#this file is for the board class
#import libraries
import random

class Board:

    #create blank board for playing
    def create_blank_board(self):
        #generate blank board to be used
        blank_board = [['-' for i in range(self.size)] for i in range(self.size)]
        return blank_board

    #display the playing board
    def display_board(self):
        top_label = '  '
        for i in range(self.size):
            top_label = top_label + str(i) + ' '
        print(top_label)

        i = 0
        for row in self.board:
            print(i, *row)
            i += 1

    #place a move on the board
    def place_move():
        pass

    #play the game
    def play_game(self):

        while True:
            #prompt for difficulty
            print("Would you like an easy game or a hard game?")
            print("     -Option 1: Easy")
            print("     -Option 2: Hard")
            option = input("Option: ")
            #create board of mines based on Option
            if option == "1":
                self.mine_board = Mine(self.create_blank_board(), self.size, self.size)
                break
            elif option == "2":
                self.mine_board = Mine(self.create_blank_board(), self.size, self.size * 2)
                break
            else:
                print("Choose a valid option")
                continue

        self.display_board()

    #################################################
    #constructor to initialize a board for the object
    def __init__(self, val = 5, board = [], mines = [], option = 1):
        if option == 1:
            self.option = option
            self.size = val
            self.board = self.create_blank_board()
        else:
            self.option = option
            self.size = val
            self.board = board
            self.mine_board = Mine(mines, option)


class Mine:
    #check the mine board in each direction


    #create the board for mines
    def create_mines(self, size):
        i = 0

        #generate mine board
        while i != self.mines:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            if self.mine_board[x][y] != 'X':
                self.mine_board[x][y] = 'X'
                i += 1
            else:
                continue

    #for testing
    #def display_board(self):
        #for row in self.mine_board:
            #print(row)

    #################################################
    #define constructor for mine board object
    def __init__(self, mines = [], size = 1, var = 1, option = 1):
        if option == 1:
            self.mines = var
            self.mine_board = mines
            self.create_mines(size)
        else:
            self.mine_board = mines

        #self.display_board()
