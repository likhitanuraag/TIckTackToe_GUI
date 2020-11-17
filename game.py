import pygame
from Board.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE
from Board.board import Board

eve = None
FPS = 120
LINE_PADDING = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tick Tack Toe")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        global eve
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            eve = event
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #pos = pygame.mouse.get_pos()
                #pos_coordinate = (pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE)
                #print(pos_coordinate)
                #pygame.draw.rect(WIN, WHITE, ((SQUARE_SIZE + LINE_PADDING)*pos_coordinate[0], (SQUARE_SIZE + LINE_PADDING)*pos_coordinate[1], SQUARE_SIZE - LINE_PADDING, SQUARE_SIZE - LINE_PADDING))

        board.draw_board(WIN, eve)
        pygame.display.update()
    
    pygame.quit()

main()