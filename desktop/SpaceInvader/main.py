import pygame as pg

# initialize the pygame object
pg.init()

#Create the screen with 800x600 resolution
screen = pg.display.set_mode((800, 600))

# Game loop
running = True 
while running:
    for event in pg.event.get(): #.event.get() is used to get the event, for example press the quit button or any other event.        if event.type == pg.QUIT:
        if event.type == pg.QUIT:    
            running = False # if we press the quit button the running goes to False and the screenis



