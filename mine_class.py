#this file is for the mine board class
#import board class
from Board_class import *

class Mine(Board):
    #define constructor for mine board object
    def __init__(self, var = 5, mines = []):
        self.size = var
        self.mine_board = mines


mine = Mine()
