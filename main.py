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

player_1 = pygame.Rect(0, 400, 40, 40)
player_2 = pygame.Rect(760, 400, 40, 40)

player_1_color = WHITE
player_2_color = WHITE

player_1_rects = []
player_2_rects = []

player_1_x = 40

runs = 10
delay = 300

font = pygame.font.Font(None, 32)

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("prisoner's dilemma")

def allways_pos():
    global player_1_x
    x = pygame.Rect(0, 400, player_1_x, 40)
    player_1_x += 80
    player_1_rects.append(x)
    print(player_1_rects)

def allways_neg():
    print("dd")

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
    
    pygame.draw.rect(win, player_2_color, player_2)
    pygame.draw.rect(win, player_1_color, player_1)

    if runs > 0:
        allways_pos()
        pygame.time.delay(delay)
        allways_neg()
        pygame.time.delay(delay)
        runs -= 1    
    
    pygame.display.flip()


pygame.quit()
sys.exit()

## Senarien mit kooperieren/konkurieren ("cooperate" is "compete")
# beide kooperieren = beide 3 points
# einer kooperiert, einer konkuriert = der konkurierende 5 points
# beide konkurieren = beide 1 point
