import pygame, sys, json
import subprocess
from time import sleep
from subprocess import call
#from Board.board import Board

BG = pygame.image.load('Assets\\bg.jpg')
MENU_BG = pygame.image.load('Assets\\mm_bg_menu.jpg')
OPT_BTN = pygame.image.load('Assets\\options_btn_s.png')
PLAY_BTN = pygame.image.load('Assets\\play_orig_btn_s.png')
EXIT_BTN = pygame.image.load('Assets\\exit_btn_s.png')
 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

eve = None
selection3 = True
selection6 = True
selection9 = True
sel_Local = True
sel_single = True
sel_multi = True
sel_lan = True
sel_back = True

WIN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tick Tack Toe")
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def spawn_program_and_die(program, exit_code=0):
        subprocess.Popen(program)
        sys.exit(exit_code)

click = False
FPS = 120
 
def main_menu():
    global click
    pygame.mixer.music.load('Assets\\sounds\\menu_1.mp3')
    pygame.mixer.music.play(-1)
    while True:
 
        WIN.blit(MENU_BG, (0, 0))
        #draw_text('main menu', font, (255, 255, 255), WIN, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(200, 300, 200, 50)
        button_2 = pygame.Rect(200, 400, 200, 50)
        button_3 = pygame.Rect(200, 500, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                sys.exit()
        #pygame.draw.rect(WIN, (255, 0, 0), button_1)
        WIN.blit(PLAY_BTN, (200, 300, 200, 50))
        #pygame.draw.rect(WIN, (255, 0, 0), button_2)
        WIN.blit(OPT_BTN, (200, 400, 200, 50))
        WIN.blit(EXIT_BTN, (200, 480, 200, 50))
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():

    spawn_program_and_die(["python", "game.py"])
    '''
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

            board.draw_board(WIN, eve)
            pygame.display.update()

    
    pygame.quit() '''

def radioButton_ini(selection, rect_name, text, xpos, ypos):
    if selection == True:
        pygame.draw.rect(WIN, (0, 0, 0), rect_name)
        draw_text(text , font, (255, 255, 255), WIN, xpos, ypos)
    else:
        pygame.draw.rect(WIN, (255, 255, 255), rect_name)
        draw_text(text , font, (0, 0, 0), WIN, xpos, ypos)   

def options():
    global click
    running = True
    while running:
        #WIN.fill((0,0,0))
        WIN.blit(BG, (0, 0))
        global selection3
        global selection6
        global selection9

        mx, my = pygame.mouse.get_pos()
        x3 = pygame.Rect(220, 50, 150, 50)
        if selection3 == True:
            pygame.draw.rect(WIN, (0, 0, 0), x3)
            draw_text('3X3', font, (255, 255, 255), WIN, 280, 70)
        else:
            pygame.draw.rect(WIN, (255, 255, 255), x3)
            draw_text('3X3', font, (0, 0, 0), WIN, 280, 70)

        x6 = pygame.Rect(220, 110, 150, 50)
        if selection6 == True:
            pygame.draw.rect(WIN, (0, 0, 0), x6)
            draw_text('6X6', font, (255, 255, 255), WIN, 280, 130)
        else:
            pygame.draw.rect(WIN, (255, 255, 255), x6)
            draw_text('6X6', font, (0, 0, 0), WIN, 280, 130)

        x9 = pygame.Rect(220, 170, 150, 50)
        if selection9 == True:
            pygame.draw.rect(WIN, (0, 0, 0), x9)
            draw_text('9X9', font, (255, 255, 255), WIN, 280, 190)
        else:
            pygame.draw.rect(WIN, (255, 255, 255), x9)
            draw_text('9X9', font, (0, 0, 0), WIN, 280, 190)
        

        draw_text('Select number of ROWS and COLUMNS in the game: ', font, (255, 255, 255), WIN, 20, 20)
        if x3.collidepoint((mx, my)):
            if click:
                selection3 = False
                selection6 = True 
                selection9 = True
                pygame.draw.rect(WIN, (255, 255, 255), x3)
                draw_text('3X3', font, (0, 0, 0), WIN, 280, 70)
                dim = {"DIM": 3}
                with open('dim-config.json', 'w') as f:  # writing JSON object
                    json.dump(dim, f)

        if x6.collidepoint((mx, my)):
            if click:
                selection3 = True
                selection6 = False 
                selection9 = True
                pygame.draw.rect(WIN, (255, 255, 255), x6)
                draw_text('6X6', font, (0, 0, 0), WIN, 280, 130)
                dim = {"DIM": 6}
                with open('dim-config.json', 'w') as f:  # writing JSON object
                    json.dump(dim, f)

        if x9.collidepoint((mx, my)):
            if click:
                selection3 = True
                selection6 = True 
                selection9 = False
                pygame.draw.rect(WIN, (255, 255, 255), x9)
                draw_text('9X9', font, (0, 0, 0), WIN, 280, 190)
                dim = {"DIM": 9}
                with open('dim-config.json', 'w') as f:  # writing JSON object
                    json.dump(dim, f)
        #-----------------------------

        global sel_Local, sel_lan, sel_multi, sel_single, sel_back

        local = pygame.Rect(220, 260, 150, 50)
        radioButton_ini(sel_Local, local, "Local-system-player", 230, 280)

        single = pygame.Rect(220, 320, 150, 50)
        radioButton_ini(sel_single, single, "Single-player (coming soon)", 230, 340)

        multi = pygame.Rect(220, 380, 150, 50)
        radioButton_ini(sel_multi, multi, "Multi-player (coming soon)", 230, 400)

        lan = pygame.Rect(220, 440, 150, 50)
        radioButton_ini(sel_lan, lan, "LAN (coming soon)", 230, 460)

        back = pygame.Rect(220, 520, 150, 50)
        radioButton_ini(sel_back, back, "BACK", 275, 540)
        

        draw_text('Select the type of the game: ', font, (255, 255, 255), WIN, 20, 230)
        if local.collidepoint((mx, my)):
            if click:
                sel_Local = False
                sel_single = True 
                sel_multi = True
                sel_lan = True
                pygame.draw.rect(WIN, (255, 255, 255), local)
                draw_text('Local-system-player', font, (0, 0, 0), WIN, 280, 270)
                gtype = {"local": True,
                            "single": False,
                            "multi": False,
                            "lan": False}
                with open('md-cnfg.json', 'w') as f:  # writing JSON object
                    json.dump(gtype, f)

        if single.collidepoint((mx, my)):
            if click:
                sel_Local = True
                sel_single = False 
                sel_multi = True
                sel_lan = True
                pygame.draw.rect(WIN, (255, 255, 255), local)
                draw_text('Single-player (coming soon)', font, (0, 0, 0), WIN, 280, 340)
                gtype = {"local": False,
                            "single": True,
                            "multi": False,
                            "lan": False}
                with open('md-cnfg.json', 'w') as f:  # writing JSON object
                    json.dump(gtype, f)

        if multi.collidepoint((mx, my)):
            if click:
                sel_Local = True
                sel_single = True 
                sel_multi = False
                sel_lan = True
                pygame.draw.rect(WIN, (255, 255, 255), multi)
                draw_text('Multi-player (coming soon)', font, (0, 0, 0), WIN, 280, 400)
                gtype = {"local": False,
                            "single": False,
                            "multi": True,
                            "lan": False}
                with open('md-cnfg.json', 'w') as f:  # writing JSON object
                    json.dump(gtype, f)

        if lan.collidepoint((mx, my)):
            if click:
                sel_Local = True
                sel_single = True 
                sel_multi = True
                sel_lan = False
                pygame.draw.rect(WIN, (255, 255, 255), lan)
                draw_text('LAN (coming soon)', font, (0, 0, 0), WIN, 280, 460)
                gtype = {"local": False,
                            "single": False,
                            "multi": False,
                            "lan": True}
                with open('md-cnfg.json', 'w') as f:  # writing JSON object
                    json.dump(gtype, f)

        if back.collidepoint((mx, my)):
            if click:
                running = False
                
        #--------------------------------
        
        #WIN.blit(PLAY_BTN, (200, 300, 200, 50))

        click = False
        #draw_text('options', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()