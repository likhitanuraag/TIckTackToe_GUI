import pygame
from .constants import WHITE, BLACK, CUSTOM, DIM, RED, SQUARE_SIZE, X_M, O_M, BG
from .player import Player

LINE_PADDING = 10

class Board:
    def __init__(self):
        self.board = []
        self.POS_CONFIG = []
        self.pos_coordinate = None
        self.X_LOC = []
        self.O_LOC = []
        self.oe_count = 0
        self.prev_pos = 0
        
    def draw_board(self, win, event):
        win.blit(BG, (0, 0))
        #pygame.draw.rect(win, WHITE, (SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #right*2 (left = 0), bottom*2 (top = 0), squ (w), squ (h)
        for xx in range(DIM):
            for yy in range(DIM):
                if (xx, yy) not in self.POS_CONFIG:
                    pygame.draw.rect(win, CUSTOM, ((SQUARE_SIZE + (LINE_PADDING - DIM))*xx, (SQUARE_SIZE + (LINE_PADDING - DIM))*yy, SQUARE_SIZE - LINE_PADDING, SQUARE_SIZE - LINE_PADDING))
                    #print("1")
                elif ((xx, yy) in self.X_LOC):
                    for loc in self.X_LOC:
                        win.blit(X_M, ((SQUARE_SIZE + (LINE_PADDING - DIM))*loc[0], (SQUARE_SIZE + (LINE_PADDING - DIM))*loc[1]))
                else:
                    for loc in self.O_LOC:
                        win.blit(O_M, ((SQUARE_SIZE + (LINE_PADDING - DIM))*loc[0], (SQUARE_SIZE + (LINE_PADDING - DIM))*loc[1]))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(self.oe_count, self.prev_pos, self.POS_CONFIG)
            if self.oe_count % 2 == 0:
                self.pos_coordinate = self.prev_pos = Player.calc_pos()
                if self.prev_pos not in self.POS_CONFIG:
                    self.POS_CONFIG.append(self.pos_coordinate)
                    self.X_LOC.append(self.pos_coordinate)
                    self.oe_count += 1
                    print(self.X_LOC)
                    #Player.validation_backend(self.X_LOC, self.POS_CONFIG)
            else:
                self.pos_coordinate = self.prev_pos = Player.calc_pos()
                if self.prev_pos not in self.POS_CONFIG:
                    self.POS_CONFIG.append(self.pos_coordinate)
                    self.O_LOC.append(self.pos_coordinate)
                    self.oe_count += 1

    def get_player_coordinates(self):
        return self.POS_CONFIG
