import pygame
from .constants import WHITE, BLACK, DIM, RED, SQUARE_SIZE, X_M, O_M

LINE_PADDING = 10
POS_CONFIG = []
pos_coordinate = None
X_LOC = []
O_LOC = []
oe_count = 0
prev_pos = 0

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        
    def draw_board(self, win, event):
        global pos_coordinate
        global oe_count
        global prev_pos
        win.fill(BLACK)
        #pygame.draw.rect(win, WHITE, (SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #right*2 (left = 0), bottom*2 (top = 0), squ (w), squ (h)
        for xx in range(DIM):
            for yy in range(DIM):
                if (xx, yy) not in POS_CONFIG:
                    pygame.draw.rect(win, WHITE, ((SQUARE_SIZE + LINE_PADDING)*xx, (SQUARE_SIZE + LINE_PADDING)*yy, SQUARE_SIZE - LINE_PADDING, SQUARE_SIZE - LINE_PADDING))
                    #print("1")
                elif ((xx, yy) in X_LOC):
                    for loc in X_LOC:
                        win.blit(X_M, ((SQUARE_SIZE + LINE_PADDING)*loc[0], (SQUARE_SIZE + LINE_PADDING)*loc[1]))
                        #print("2")
                else:
                    for loc in O_LOC:
                        win.blit(O_M, ((SQUARE_SIZE + LINE_PADDING)*loc[0], (SQUARE_SIZE + LINE_PADDING)*loc[1]))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(oe_count, prev_pos, POS_CONFIG)
            if oe_count % 2 == 0:
                pos = pygame.mouse.get_pos()
                pos_coordinate = (pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE)
                prev_pos = pos_coordinate
                if prev_pos not in POS_CONFIG:
                    POS_CONFIG.append(pos_coordinate)
                    X_LOC.append(pos_coordinate)
                    oe_count += 1
                    #print(POS_CONFIG)
            else:
                pos = pygame.mouse.get_pos()
                pos_coordinate = (pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE)
                prev_pos = pos_coordinate
                if prev_pos not in POS_CONFIG:
                    POS_CONFIG.append(pos_coordinate)
                    O_LOC.append(pos_coordinate)
                    oe_count += 1
                    #print(POS_CONFIG)
