#this file is for the board class

class Board(object):
    #constructor to initialize a board for the object
    def __init__(self, val):
        self.board = []
        self.size = val

    #create blank board for playing
    def create_blank_board(self):
        #generate blank board to be used
        blank_board = [['-' for i in range(self.size)] for i in range(self.size)]
        return blank_board

    #display the playing board
    def display_board(self):
        self.board = self.create_blank_board(self)
        for row in self.board:
            print(row)

def main():
    board1 = Board(5)
    board1.display_board(board1)

main()
