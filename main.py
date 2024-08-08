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

player_1_x = 0
player_1_y = 300

player_2_x = 0
player_2_y = 500

p1_red = False
p2_red = False

p1_score = 0
p2_score = 0

rects_margin = 80

runs = 10
delay = 300

font = pygame.font.Font(None, 32)

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Prisoner's Dilemma")

def allways_pos():
    global player_1_x
    p1_template = pygame.Rect(player_1_x, player_1_y, 40, 40)
    player_1_x += rects_margin
    player_1_rects.append(p1_template)

def allways_neg():
    global player_2_x
    p2_template = pygame.Rect(player_2_x, player_2_y, 40, 40)
    player_2_x += rects_margin
    player_2_rects.append(p2_template)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill(BLACK)

    player_1_header = font.render("Player 1: " + str(p1_score), True, WHITE)
    player_1_header_rect = player_1_header.get_rect(topleft=(10, 10))
    win.blit(player_1_header, player_1_header_rect)

    player_2_header = font.render("Player 2: " + str(p2_score), True, WHITE)
    player_2_header_rect = player_2_header.get_rect(topleft=(650, 10))
    win.blit(player_2_header, player_2_header_rect)

    p1_red = False
    for rect in player_1_rects:
        pygame.draw.rect(win, GREEN, rect)
        p1_red = False

    p2_red = True
    for rect in player_2_rects:
        pygame.draw.rect(win, RED, rect)
        p2_red = True

    if runs > 0:
        allways_pos()
        pygame.time.delay(delay)
        allways_neg()
        pygame.time.delay(delay)
        runs -= 1

    if not p1_red and not p2_red:
        p1_score += 3
        p2_score += 3
    elif not p1_red and p2_red:
        p2_score += 5
    elif p1_red and not p2_red:
        p1_score += 5
    elif p1_red and p2_red:
        p1_score += 1
        p2_score += 1
    
    pygame.display.flip()

pygame.quit()
sys.exit()
