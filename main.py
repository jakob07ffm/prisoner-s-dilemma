import pygame
import sys
import time

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 32)

win_width = 800
win_height = 800

rounds = 10
runs = 0

#Var die zeigt ob rot grün(kooperieren oder konkurenz)
# 0 = konkurieren, 1 = kooperieren
p1 = None
p2 = None

p1_score = 0
p2_score = 0

p1_decisions = []
p2_decisions = []

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("prisoner's dilemma")

def p1_choise():
    p1 = 0
    p1_decisions.append(p1)

def p2_choise():
    p2 = 1
    if runs >= 1:
        if p1_decisions[runs] == 0:
            p2 = 0
    p2_decisions.append(p2)

def points():
    global p1_score, p2_score
    # Funktion die die Punkte vergibt:

    #beide Partein kooperieren
    if p1_decisions[runs] == 1 and p2_decisions[runs] == 1:
        p1_score += 3
        p2_score += 3

    #einer der Beiden kooperiert und der andere nicht
    if p1_decisions[runs] == 1 and p2_decisions[runs] == 0:
        p2_score += 5
    if p2_decisions[runs] == 1 and p1_decisions[runs]== 0:
        p1_score += 5

    #beide Partein konkurieren
    if p1_decisions[runs] == 0 and p2_decisions[runs] == 0:
        p1_score += 1
        p2_score += 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill(BLACK)

    p1_choise()
    p2_choise()
    points()

    print(runs)
    print(p1_decisions)
    print(p2_decisions)
    print(p1_score, p2_score)

    runs += 1
    pygame.display.flip()

    if runs >= rounds:
        running = False

pygame.quit()
sys.exit()


# 1 = Green
# 0 = Red


#todo
# - vielleicht return statement benutzen
# - Neue Syteme / Algorüthmen finden + ihre Namen
# - Das Belohnungssystem erstelle(score) #
# - Gerade handel p2 mit dem wissen was p1 gewählt hat.#
