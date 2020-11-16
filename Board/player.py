from .constants import SQUARE_SIZE

class Player:
    PADDING  = 10
    BORDER = 2

    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player
        self.x = 0
        self.y = 0

def calc_pos(self):
    self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
    self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

