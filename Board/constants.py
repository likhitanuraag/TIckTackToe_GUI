import pygame

WIDTH, HEIGHT = 600, 600
DIM = 3
SQUARE_SIZE = WIDTH//DIM
X_L = pygame.image.load('Assets\\x_l.png')
X_S = pygame.image.load('Assets\\x_s.png')
X_M = pygame.image.load('Assets\\x_m.png')
O_L = pygame.image.load('Assets\\o_l.png')
O_S = pygame.image.load('Assets\\o_s.png')
O_M = pygame.image.load('Assets\\o_m.png')
BG = pygame.image.load('Assets\\bg.jpg')
XES = pygame.image.load('Assets\\x_wins.jpg')
OES = pygame.image.load('Assets\\o_wins.jpg')

RED, WHITE, BLACK, BLUE, CUSTOM = (255, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 255), (200, 204, 213)