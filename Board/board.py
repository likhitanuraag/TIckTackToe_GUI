import pygame
from .constants import WHITE, BLACK, DIM, RED, SQUARE_SIZE

LINE_PADDING = 10

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        
    def draw_board(self, win):
        win.fill(BLACK)
        #pygame.draw.rect(win, WHITE, (SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #right*2 (left = 0), bottom*2 (top = 0), squ, squ
        for xx in range(DIM):
            for yy in range(DIM):
                pygame.draw.rect(win, WHITE, ((SQUARE_SIZE + LINE_PADDING)*xx, (SQUARE_SIZE + LINE_PADDING)*yy, SQUARE_SIZE - LINE_PADDING, SQUARE_SIZE - LINE_PADDING))