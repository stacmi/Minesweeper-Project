#this file is for the board class
#import mine class
from mine_class import *

class Board:

    #create blank board for playing
    def create_blank_board(self):
        #generate blank board to be used
        blank_board = [['-' for i in range(self.size)] for i in range(self.size)]
        return blank_board

    #display the playing board
    def display_board(self):
        for row in self.board:
            print(row)



    #################################################
    #constructor to initialize a board for the object
    def __init__(self, val = 5, board = []):
        self.size = val
        self.board = self.create_blank_board()
        self.mine = Mine(val, self.board)


class Mine(Board):
    #define constructor for mine board object
    def __init__(self, mines = []):
        self.mines = self.create_blank_board()

def main():
    board1 = Board(10)
    board1.display_board()

main()
