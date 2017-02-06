import pygame
from pygame import *


window_width = 800
window_height = 600
display = (window_width, window_height)
background_color = "#004400"





def main():
    pygame.init()
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("Ideco BattleCity")
    bg = Surface((window_width, window_height))

    bg.fill(Color(background_color))

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            screen.blit(bg, (0, 0))
            pygame.display.update()





if __name__ == '__main__':
    main()