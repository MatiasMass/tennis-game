import pygame, sys

def terminate():
    pygame.quit()
    sys.exit()

def draw_text(text, font, surface, x, y, TEXTCOLOR):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)