'''Make a programe that:
    sets a green square window
    takes user input to move orange square around
    '''

import os
import pygame as pg


'''# quick function to load an image
def load_image(name):
    path = os.path.join(main_dir, "data", name)
    return pg.image.load(path).convert()'''

white = (255,255,255) #3
red = (255,0,0) #4
green = (0,255,0) #5

class Sprite(pg.sprite.Sprite):
    def __init__(self, color, height, width):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        # make a small square sprite
        self.rect = pg.draw.rect(self, white, (25,25,25))
    # def update(self):
    #     #apparently this moves sprite based on mouse
    #     pos = pg.mouse.get_pos()
    #     self.rect.topleft = pos

def main():
    pg.init()
    # set up a 700 x 700 screen 
    screen = pg.display.set_mode((700, 700))
    #turns screen red
    screen.fill(red)
    #updates the screen
    pg.display.flip()
    #labels window
    pg.display.set_caption("Move it!")

    all_sprites = pg.sprite.Group()
    clock = pg.time.Clock()
    run = True
    
    while run:
        Sprite.rect.x = 250
        Sprite.rect.y = 250
        all_sprites.add(Sprite)
        all_sprites.update()
        all_sprites.draw(screen)
        pg.display.flip()
        #sets up operations
        clock.tick(60)
        pos = pg.mouse.get_pos()
        Sprite.rect.x = pos[0]
        Sprite.rect.y = pos[1]
        
        
        #exit conditions
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                run = False
        sprites_list = pg.sprite.Group()
        

if __name__ == "__main__":
    main()
