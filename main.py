import pygame
from pygame import *

window_width = 830
window_height = 830
display = (window_width, window_height)
background_color = "#004400"  # Green BG

# bricks vars
brick_width = 32
brick_height = 32
brick_color = "#FF6262"


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

            #  creating bricks
            x = y = 0
            for row in level:
                for col in row:
                    if col == "#":
                        #  Create block and fill with color
                        br = Surface((brick_width, brick_height))
                        br.fill(Color(brick_color))
                        screen.blit(br, (x, y))

                    x += brick_width
                y += brick_height
                x = 0
            pygame.display.update()

if __name__ == '__main__':
    level = [
        "..........................",
        "..........................",
        "..##..##..##..##..##..##..",
        "..##..##..##..##..##..##..",
        "..##..##..##..##..##..##..",
        "..##..##..##..##..##..##..",
        "..##..##..##@@##..##..##..",
        "..##..##..##@@##..##..##..",
        "..##..##..##..##..##..##..",
        "..##..##..........##..##..",
        "..##..##..........##..##..",
        "..........##..##..........",
        "..........##..##..........",
        "##..####..........####..##",
        "@@..####..........####..@@",
        "..........##..##..........",
        "..........######..........",
        "..##..##..######..##..##..",
        "..##..##..##..##..##..##..",
        "..##..##..##..##..##..##..",
        "..##..##..##..##..##..##..",
        "..##..##..........##..##..",
        "..##..##..........##..##..",
        "..##..##...####...##..##..",
        "...........#..#...........",
        "...........#..#..........."]

    main()