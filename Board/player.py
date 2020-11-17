import pygame
from .constants import SQUARE_SIZE, DIM

class Player:
    PADDING  = 10
    BORDER = 2

    def __init__(self, dim, player):
        self.dim = dim
        self.player = player
        self.x = "X"
        self.o = "O"

        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.dim + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.dim + SQUARE_SIZE // 2

    def player_turn(self, player):
        for game_loop in DIM*DIM:
            if game_loop % 2 == 0:
                pass # Even 
            else:
                pass # Odd


    def __repr__(self):
        return str(self.player)

