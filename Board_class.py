#this file is for the board class
#import mine class

class Board:

    #create blank board for playing
    def create_blank_board(self):
        #generate blank board to be used
        blank_board = [['-' for i in range(self.size)] for i in range(self.size)]
        return blank_board

    #display the playing board
    def display_board(self):
        print("")
        for row in self.board:
            print(row)

    #play the game
    def play_game(self):
        #prompt for difficulty
        print("Would you like an easy game or a hard game?")
        print()

        self.display_board()

    #################################################
    #constructor to initialize a board for the object
    def __init__(self, val = 5, board = []):
        self.size = val
        self.board = self.create_blank_board()


class Mine:
    def create_mines(self):
        pass

    def create_mines(self):
        i = 0
        number_of_mines = size - 1

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

    #for testing
    #def display_board(self):
    #    for row in self.mine_board:
    #        print(row)




    #################################################
    #define constructor for mine board object
    def __init__(self, var = 5, mines = []):
        self.mines = var
        self.mine_board = mines
        self.display_board()
