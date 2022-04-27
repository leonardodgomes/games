import pygame as pg
import random

# initialize the pygame object
pg.init()

#Create the screen with 800x600 resolution
screen = pg.display.set_mode((800, 600))

# Title for the game
pg.display.set_caption(" Samuel - Space Invaders")

#Icon for the game
icon = pg.image.load("assets/gps_icon32.png")
pg.display.set_icon(icon)

#Backgroud for the game
bground = pg.image.load("assets/gps_backgroud.png")

#Player
player_img = pg.image.load("assets/gps_ship.png") # load the image
player_x = 370
player_y = 480
playerX_change = 0 # to control de movement of the ship

#Bullet - You cannot see the bullet on the screen
#Fire - Theb bullet is currenty moving
bulletImg = pg.image.load("assets/gps_bullet.png")
bullet_x = 0
bullet_y = 480
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready" # to control the bullet. If ready then the bullet is following the ship, when change to fire, the bullet start the X movement

#Enemy
enemy_img = pg.image.load("assets/gps_ufo_red.png") # load the image
enemy_x = random.randint(0,800)
enemy_y = random.randint(0, 160)
enemyX_change = 4
enemyY_change = 40



# Define the function to the player
def player(x,y):
    screen.blit(player_img, (x, y))

# Define the function to the enemy
def enemy(x,y):
    screen.blit(enemy_img, (x, y))

# Define the function to the bullet
def fire_bullet(x,y):
    global bullet_state #make this variable global
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10)) #add some pixels to centralize the bullet 


# Game loop
running = True 
while running:
    
    #   Define the color of the screen - RGB color
    screen.fill((0 , 0, 0))
    
    # Backgroud Image
    screen.blit(bground,(0,0))
        
    for event in pg.event.get(): #.event.get() is used to get the event, for example press the quit button or any other event.        if event.type == pg.QUIT:
        if event.type == pg.QUIT:    
            running = False # if we press the quit button the running goes to False and the screenis

#       If the keystroke is pressed, check if was the LEFT or RIGTH
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change = -5
#                print("Left")
            if event.key == pg.K_RIGHT:
                playerX_change = 5
#                print("Right")
            if event.key == pg.K_SPACE:
                fire_bullet(player_x,bullet_y)
#                print("Space")
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.type == pg.K_RIGHT:
                playerX_change = 0
#                print("Up")
    
#   Change the position of the ship        
    player_x += playerX_change

#   Control the boudaries of the screen. the ship cannot p+ass the 0 and the 700        
    if player_x <= 0:
        player_x = 0
    if player_x >= 742:
        player_x = 742    


#   Movments of the enemy
    enemy_x += enemyX_change

#   Control the boudaries of the screen. When the enemy hit the boudaries they change the direction  
    if enemy_x <= 0:
        enemyX_change = 4
        enemy_y += enemyY_change
    if enemy_x >= 742:
        enemyX_change = -4 
        enemy_y += enemyY_change


#   Bullet Movment
    if bullet_state is "fire":
        fire_bullet(player_x, bullet_y)
        bullet_y -= bulletY_change


#   Call the player function
    player(player_x, player_y)    
    
    
#   Call the enemty function
    enemy(enemy_x, enemy_y)    
    
#   to work properly we need to add a update function
    pg.display.update()


