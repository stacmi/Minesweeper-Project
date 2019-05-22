#this file is for the mine board class
#import board class
from board_class import *

class Mine(Board):
    #define constructor for mine board object
    def __init__(self, mines = []):
        self.mines = self.create_blank_board()

mine = Mine()
