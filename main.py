import pygame
import sys
import time

pygame.init()

win_width = 800
win_height = 800

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

player_1_color = WHITE
player_2_color = WHITE

player_1_rects = []
player_2_rects = []

player_1_color = []
player_2_color = []

player_1_x = 0
player_1_y = 300

player_2_x = 0
player_2_y = 500

rects_margin = 80

runs = 10
delay = 300

font = pygame.font.Font(None, 32)

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("prisoner's dilemma")

def allways_pos():
    global player_1_x, p1_color
    p1_template = pygame.Rect(player_1_x, player_1_y, 40, 40)
    player_1_x += rects_margin
    player_1_rects.append(p1_template)
    p1_color = GREEN
    player_1_color.append(p1_color)
    print(player_1_color)

def allways_neg():
    global player_2_x, p2_color
    p2_template = pygame.Rect(player_2_x, player_2_y, 40, 40)
    player_2_x += rects_margin
    player_2_rects.append(p2_template)
    p2_color = RED
    player_2_color.append(p2_color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill(BLACK)

    player_1_header = (font.render("Player 1:", True, WHITE))
    player_1_header_rect = player_1_header.get_rect()
    win.blit(player_1_header, player_1_header_rect)

    player_2_header = (font.render("Player 2:", True, WHITE))
    player_2_header_rect = player_2_header.get_rect()
    player_2_header_rect.topleft = (650, 0)
    win.blit(player_2_header, player_2_header_rect)
    

    #for rect, color in player_1_rects:
    #   count = 0
    #   pygame.draw.rect(win, (p1_color[count]), rect)
    #   count += 1
    for rect in player_1_rects:
        pygame.draw.rect(win, GREEN, rect)
    
    for rect in player_2_rects:
        pygame.draw.rect(win, RED, rect)

    if runs > 0:
        allways_pos()
        pygame.time.delay(delay)
        allways_neg()
        pygame.time.delay(delay)
        runs -= 1

    ## Punkte vergabe
    #for r1c, r2c in zip(player_1_rects, player_2_rects):
        
    
    pygame.display.flip()


pygame.quit()
sys.exit()

## Senarien mit kooperieren/konkurieren ("cooperate" is "compete")
# beide kooperieren = beide 3 points
# einer kooperiert, einer konkuriert = der konkurierende 5 points
# beide konkurieren = beide 1 point


## TODO
# - Das delay wird bei dem letzten spawnen der rects nicht beachtet
