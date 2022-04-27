import pygame as pg

# initialize the pygame object
pg.init()

#Create the screen with 800x600 resolution
screen = pg.display.set_mode((800, 600))

# Title for the game
pg.display.set_caption(" Samuel - Space Invaders")

#Icon for the game
icon = pg.image.load("assets/gps_icon32.png")
pg.display.set_icon(icon)


# Game loop
running = True 
while running:
    for event in pg.event.get(): #.event.get() is used to get the event, for example press the quit button or any other event.        if event.type == pg.QUIT:
        if event.type == pg.QUIT:    
            running = False # if we press the quit button the running goes to False and the screenis

#   Define the color of the screen - RGB color
    screen.fill((19 , 0, 77))
#   to work properly we need to add a update function
    pg.display.update()


