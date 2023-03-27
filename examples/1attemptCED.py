'''Make a programe that:
    sets a green square window
    takes user input to move orange square around
    '''

import os
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        #TODO:figure out how to make a small square sprite
        self.rect = pg.draw.rect()
    def update(self):
        #apparently this moves sprite based on mouse
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos

def main():
    #why is there a pylance error?
    pygame.init()
    #should set up a 700 x 700 screen 
    screen = pygame.display.set_mode((700, 700))
    #turns screen bluish green
    screen.fill((0, 250, 50))
    #labels window
    pg.display.set_caption("Move it!")
    clock = pg.time.Clock()
    run = True

    while run:
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
