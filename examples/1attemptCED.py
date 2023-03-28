'''Make a programe that:
    sets a green square window
    takes user input to move orange square around
    '''

import os
import pygame as pg
from pygame.draw import polygon

white = (255, 255, 255)  #3
red = (255, 0, 0)  #4
green = (0, 255, 0)  #5

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500


# Object class
class Sprite(pg.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pg.draw.rect(self.image, color, pg.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()


# class Player(pg.sprite.Sprite):

#     def __init__(self):
#         pg.sprite.Sprite.__init__(self)  # call Sprite initializer
#         # super().__init__()

#         #TODO:figure out how to make a small square sprite
#         self.rect = pg.draw.rect(self, 'red')

#     def update(self):
#         #apparently this moves sprite based on mouse
#         pos = pg.mouse.get_pos()
#         self.rect.topleft = pos


def main():
    pg.init()
    #should set up a 700 x 700 screen
    screen = pg.display.set_mode((700, 700))
    #turns screen blue
    screen.fill(red)
    #labels window
    pg.display.set_caption("Move it!")
    clock = pg.time.Clock()
    run = True

    while run:
        screen.fill("blue")
        #sets up operations
        clock.tick(60)
        #exit conditions
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                run = False


if __name__ == "__main__":
    main()
