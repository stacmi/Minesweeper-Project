#this file is for the board class

class Board:
    #constructor to initialize a board for the object
    def __init__(self, size):
        self.board = []
        self.size = size

    #create blank board for playing
    def create_blank_board():
        #generate blank board to be used
        blank_board = [['-' for i in range(self.size)] for i in range(self.size)]
        return blank_board

    #display the playing board
    def display_board():
        self.board = create_blank_board()
        for row in self.board:
            print(row)

def main():
    board = Board(5)
    board.display_board()

main()
