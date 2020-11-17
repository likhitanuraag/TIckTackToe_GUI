import pygame
from .constants import SQUARE_SIZE, DIM
#from .board import Board

class Player:
    PADDING  = 10
    BORDER = 2

    def __init__(self, dim, winner):
        self.dim = dim
        self.winner = winner
        self.calc_pos()

    def calc_pos():
        pos = pygame.mouse.get_pos()
        return (pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE)
    
    def validation_backend(player, config):
        pass        

    def __repr__(self):
        return str(self.player)
