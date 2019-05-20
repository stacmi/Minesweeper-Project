#this file is for the board class

class Board():
    #constructor to initialize a board for the object
    def __init__(self, size):
        self.board = create_blank_board(size)
        self.size = size

    #create blank board for playing
    def create_blank_board(size):
        #generate blank board to be used
        blank_board = [['-' for i in range(size)] for i in range(size)]
        return blank_board

    #display the playing board
    def display_board():
        for row in self.board:
            print(row)

board = Board()

board.display_board()
