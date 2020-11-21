import pygame
from .constants import SQUARE_SIZE, DIM, X_M, O_M, X_S, O_S, X_MS, O_MS

class Player:
    def __init__(self):
        self.calc_pos()

    def player_asset_selector(DIM, player):
        if DIM == 3 and player == "X":
            return X_M
        if DIM == 6 and player == "X":
            return X_MS
        if DIM == 9 and player == "X":
            return X_S
        if DIM == 3 and player == "O":
            return O_M
        if DIM == 6 and player == "O":
            return O_MS
        if DIM == 9 and player == "O":
            return O_S

    def calc_pos():
        pos = pygame.mouse.get_pos()
        return (pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE)
    
    def validation_backend(player):

        for row in range(len(player)): ##Horizontal check
            pos_lock = []
            for col in range(len(player)):
                if player[col][1] == row:
                    pos_lock.append(player[col][1])
                    if len(pos_lock) == DIM:
                        return True
        
        for col in range(len(player)): ##Vertical check
            pos_lock = []
            for row in range(len(player)):
                if player[row][0] == col:
                    pos_lock.append(player[row][0])
                    if len(pos_lock) == DIM:
                        return True
        pos_lock = []
        for xx in range(len(player)): ##RightDownDiagonal check
            #print("xx: ", xx, "player: ", player)
            if player[xx][0] == player[xx][1] and player[xx][1] == player[xx][0]:
                pos_lock.append(xx)
                if len(pos_lock) == DIM:
                    return True

        pos_lock = []
        for yy in range(len(player)): ##LeftDownDiagonal check
            add = player[yy][0] + player[yy][1]
            if add == (DIM-1):
                pos_lock.append(add)
                if len(pos_lock) == DIM:
                    return True

    def __repr__(self):
        return str(self.player)
