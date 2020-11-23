import pygame
import subprocess
from time import sleep
from subprocess import call
import sys
from .constants import CUSTOM, DIM, SQUARE_SIZE, BG, XES, OES, DRAW
from .player import Player

LINE_PADDING = 10
X_WIN = 0
O_WIN = 0

pygame.mixer.init()

class Board:
    def __init__(self):
        self.board = []
        self.POS_CONFIG = []
        self.pos_coordinate = None
        self.X_LOC = []
        self.O_LOC = []
        self.oe_count = 0
        self.prev_pos = 0

    def spawn_program_and_die(program, exit_code=0):
        subprocess.Popen(program)
        sys.exit(exit_code)
    
    def game_end_window(window, p_win):
        if p_win == "X":
            while True:
                window.blit(XES, (0, 0))
                pygame.display.update()
                x_win = 0
                pygame.mixer.music.load('Assets\\sounds\\x_win_sound.mp3')
                pygame.mixer.music.play()
                sleep(8)
                Board.spawn_program_and_die(["python", "menu.py"])
        if p_win == "O":
            while True:
                window.blit(OES, (0, 0))
                pygame.display.update()
                o_win = 0
                pygame.mixer.music.load('Assets\\sounds\\o_win.mp3')
                pygame.mixer.music.play()
                sleep(8)
                Board.spawn_program_and_die(["python", "menu.py"])
        if p_win == "DRAW":
            while True:
                window.blit(DRAW, (0, 0))
                pygame.display.update()
                pygame.mixer.music.load('Assets\\sounds\\draw_sound.mp3')
                pygame.mixer.music.play()
                sleep(8)
                Board.spawn_program_and_die(["python", "menu.py"])

    def DRAW_check(win, all_coordinates, dim):
        if int(len(all_coordinates)) == dim*dim:
            print("Its a DRAW!")
            Board.game_end_window(win, "DRAW")

    def draw_board(self, win, event):
        global X_WIN
        global O_WIN
        win.blit(BG, (0, 0))
        #pygame.draw.rect(win, WHITE, (SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #right*2 (left = 0), bottom*2 (top = 0), squ (w), squ (h)
        for xx in range(DIM):
            for yy in range(DIM):
                if (xx, yy) not in self.POS_CONFIG:
                    pygame.draw.rect(win, CUSTOM, ((SQUARE_SIZE + (LINE_PADDING - DIM))*xx, (SQUARE_SIZE + (LINE_PADDING - DIM))*yy, SQUARE_SIZE - LINE_PADDING, SQUARE_SIZE - LINE_PADDING))
                elif ((xx, yy) in self.X_LOC):
                    for loc in self.X_LOC:
                        win.blit(Player.player_asset_selector(DIM, "X"), ((SQUARE_SIZE + (LINE_PADDING - DIM))*loc[0], (SQUARE_SIZE + (LINE_PADDING - DIM))*loc[1]))
                else:
                    for loc in self.O_LOC:
                        win.blit(Player.player_asset_selector(DIM, "O"), ((SQUARE_SIZE + (LINE_PADDING - DIM))*loc[0], (SQUARE_SIZE + (LINE_PADDING - DIM))*loc[1]))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.oe_count % 2 == 0:
                self.pos_coordinate = self.prev_pos = Player.calc_pos()
                if self.prev_pos not in self.POS_CONFIG:
                    self.POS_CONFIG.append(self.pos_coordinate)
                    self.X_LOC.append(self.pos_coordinate)
                    self.oe_count += 1
                    pygame.mixer.music.load('Assets\\sounds\\btn.mp3')
                    pygame.mixer.music.play()
                    X_WIN = Player.validation_backend(self.X_LOC)
                    if X_WIN == True:
                        print("X wins")
                        Board.game_end_window(win, "X")
                    Board.DRAW_check(win, self.POS_CONFIG, DIM)
            else:
                self.pos_coordinate = self.prev_pos = Player.calc_pos()
                if self.prev_pos not in self.POS_CONFIG:
                    self.POS_CONFIG.append(self.pos_coordinate)
                    self.O_LOC.append(self.pos_coordinate)
                    self.oe_count += 1
                    pygame.mixer.music.load('Assets\\sounds\\btn.mp3')
                    pygame.mixer.music.play()
                    O_WIN = Player.validation_backend(self.O_LOC)
                    if O_WIN == True:
                        print("O wins")
                        Board.game_end_window(win, "O")
                    Board.DRAW_check(win, self.POS_CONFIG, DIM)
                
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Board.spawn_program_and_die(["python", "menu.py"])
            
    
    def get_player_coordinates(self):
        return self.POS_CONFIG
