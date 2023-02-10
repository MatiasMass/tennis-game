import sys
import os
import random
import pygame
from pygame.locals import *
from functions import *

if __name__ == '__main__':
    pygame.init()

    # PATH
    path = os.getcwd()

    # Join various path components
    IMAGE_PATH = os.path.join(path, "tennis-court-2.png")
    print(IMAGE_PATH)

    # COLORS
    BLACK = (0, 0, 0)
    BLUE = (0, 80, 200)
    WHITE = (255, 255, 255)


    # SCREEN
    WINDOWHEIGHT = 650
    WINDOWWIDTH = 348
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('TENNIS GAME')
    FPS = 60
    mainClock = pygame.time.Clock()
    imp = pygame.image.load(IMAGE_PATH).convert()
    windowSurface.blit(imp, (0, 0))

    # PLAYERS
    PLAYERWIDTH = 100
    PLAYERHEIGHT = 20
    # left, top, width, height
    PLAYER1_LEFT_POSITION = ((WINDOWWIDTH / 2) - PLAYERWIDTH / 2)
    PLAYER1 = {'rect': pygame.Rect(PLAYER1_LEFT_POSITION, 10, PLAYERWIDTH, PLAYERHEIGHT),
            'color': BLUE}
    PLAYER2_LEFT_POSITION = ((WINDOWWIDTH / 2) - PLAYERWIDTH / 2)
    PLAYER2 = {'rect': pygame.Rect(PLAYER2_LEFT_POSITION, WINDOWHEIGHT - PLAYERHEIGHT - 10, PLAYERWIDTH, PLAYERHEIGHT),
            'color': BLUE}

    PLAYERSPEED = 10
    moveLeftPLAYER1 = moveRightPLAYER1 = False
    moveLeftPLAYER2 = moveRightPLAYER2 = False
    MOVESPEED = 5

    # BALL
    DOWNLEFT = 'downleft'
    DOWNRIGHT = 'downright'
    UPLEFT = 'upleft'
    UPRIGHT = 'upright'

    DIRECTIONS = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

    BALLSIZE = 10

    # SHOW THE START SCREEN
    font = pygame.font.SysFont(None, 100)
    scorePlayer1 = 0
    scorePlayer2 = 0
    TEXTCOLOR = (255, 255, 255)


    while True:

        RANDOMDIRECT = random.randint(0, len(DIRECTIONS) - 1)

        BALL = {'rect': pygame.Rect((WINDOWWIDTH / 2), (WINDOWHEIGHT / 2), BALLSIZE, BALLSIZE),
                'color': WHITE,
                'dir': DIRECTIONS[RANDOMDIRECT]}

        while True:

            for event in pygame.event.get():

                if event.type == QUIT:
                    terminate()

                if event.type == KEYDOWN:
                    if event.key == K_d:
                        moveRightPLAYER1 = True
                        moveLeftPLAYER1 = False
                    if event.key == K_a:
                        moveLeftPLAYER1 = True
                        moveRightPLAYER1 = False
                    if event.key == K_RIGHT:
                        moveRightPLAYER2 = True
                        moveLeftPLAYER2 = False
                    if event.key == K_LEFT:
                        moveLeftPLAYER2 = True
                        moveRightPLAYER2 = False

                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()
                    if event.key == K_d:
                        moveRightPLAYER1 = False
                    if event.key == K_a:
                        moveLeftPLAYER1 = False
                    if event.key == K_RIGHT:
                        moveRightPLAYER2 = False
                    if event.key == K_LEFT:
                        moveLeftPLAYER2 = False
                    if event.key == K_x:
                        MOVESPEED += 1
                    if event.key == K_z:
                        MOVESPEED -= 1

            # MOVE BALL

            if BALL['dir'] == DOWNLEFT:
                BALL['rect'].left -= MOVESPEED
                BALL['rect'].top += MOVESPEED

            if BALL['dir'] == DOWNRIGHT:
                BALL['rect'].left += MOVESPEED
                BALL['rect'].top += MOVESPEED

            if BALL['dir'] == UPLEFT:
                BALL['rect'].left -= MOVESPEED
                BALL['rect'].top -= MOVESPEED

            if BALL['dir'] == UPRIGHT:
                BALL['rect'].left += MOVESPEED
                BALL['rect'].top -= MOVESPEED

            if BALL['rect'].left < 0:
                if BALL['dir'] == UPLEFT:
                    BALL['dir'] = UPRIGHT
                if BALL['dir'] == DOWNLEFT:
                    BALL['dir'] = DOWNRIGHT

            if BALL['rect'].right > WINDOWWIDTH:
                if BALL['dir'] == UPRIGHT:
                    BALL['dir'] = UPLEFT
                if BALL['dir'] == DOWNRIGHT:
                    BALL['dir'] = DOWNLEFT

            if BALL['rect'].bottom < 0:
                scorePlayer2 += 1
                break

            if BALL['rect'].top > WINDOWHEIGHT:
                scorePlayer1 += 1
                break

            if BALL['rect'].colliderect(PLAYER1['rect']) or BALL['rect'].colliderect(PLAYER2['rect']):
                if BALL['rect'].top <= PLAYER1['rect'].bottom:
                    if BALL['dir'] == UPRIGHT:
                        BALL['dir'] = DOWNRIGHT
                    if BALL['dir'] == UPLEFT:
                        BALL['dir'] = DOWNLEFT
                elif BALL['rect'].top <= PLAYER2['rect'].top:
                    if BALL['dir'] == DOWNRIGHT:
                        BALL['dir'] = UPRIGHT
                    if BALL['dir'] == DOWNLEFT:
                        BALL['dir'] = UPLEFT

            # windowSurface.fill(BLACK)

            if moveRightPLAYER1 and PLAYER1['rect'].right < WINDOWWIDTH:
                PLAYER1['rect'].move_ip(PLAYERSPEED, 0)
            if moveLeftPLAYER1 and PLAYER1['rect'].left > 0:
                PLAYER1['rect'].move_ip(- 1 * PLAYERSPEED, 0)

            if moveRightPLAYER2 and PLAYER2['rect'].right < WINDOWWIDTH:
                PLAYER2['rect'].move_ip(PLAYERSPEED, 0)
            if moveLeftPLAYER2 and PLAYER2['rect'].left > 0:
                PLAYER2['rect'].move_ip(- 1 * PLAYERSPEED, 0)

            # WINDOWSURFACE DRAW
            windowSurface.blit(imp, (0, 0))

            # PLAYERS DRAW
            pygame.draw.rect(windowSurface, PLAYER1['color'], PLAYER1['rect'])
            pygame.draw.rect(windowSurface, PLAYER2['color'], PLAYER2['rect'])

            pygame.draw.rect(windowSurface, BALL['color'], BALL['rect'])

            draw_text('%s' % (scorePlayer1), font,
                    windowSurface, WINDOWWIDTH / 2 - 15, 100, WHITE)
            draw_text('%s' % (scorePlayer2), font, windowSurface,
                    WINDOWWIDTH / 2 - 20, WINDOWHEIGHT - 150, WHITE)

            pygame.display.update()

            mainClock.tick(FPS)


