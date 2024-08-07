import pygame
import sys

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

player_1_decisions = []
player_2_decisions = []

runs = 10

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("prisoner's dilemma")

def allways_pos():
    

def allways_neg():
    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill(BLACK)
    
    pygame.draw.rect(win, player_1_color, player_1)
    pygame.draw.rect(win, player_2_color, player_2)
    
    pygame.display.flip()


pygame.quit()
sys.exit()

## Senarien mit kooperieren/konkurieren ("cooperate" is "compete")
# beide kooperieren = beide 3 points
# einer kooperiert, einer konkuriert = der konkurierende 5 points
# beide konkurieren = beide 1 point
