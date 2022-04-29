from ctypes.wintypes import PMSG
import pygame as pg
from pygame import mixer

import random
import math #to colision calculations

# initialize the pygame object
pg.init()

#Screen -----------------------------------------------

#Create the screen with 800x600 resolution
screen = pg.display.set_mode((800, 600))

#Caption for the game
pg.display.set_caption(" Samuel - Space Invaders")

#Icon for the game
icon = pg.image.load("assets/gps_icon32.png")
pg.display.set_icon(icon)

#Backgroud for the game
bground = pg.image.load("assets/gps_backgroud.png")

#Backgroud Sound
mixer.music.load("assets/background.wav")
mixer.music.play(-1)

#Player -----------------------------------------------

player_img = pg.image.load("assets/gps_ship.png") # load the image
player_x = 370
player_y = 480
playerX_change = 0 # to control de movement of the ship

#Bullet------------------------------------------------
# Ready - You cannot see the bullet on the screen
# Fire  - Theb bullet is currenty moving

bulletImg = pg.image.load("assets/gps_bullet.png")
bullet_x = 0
bullet_y = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" # to control the bullet. If ready then the bullet is following the ship, when change to fire, the bullet start the X movement


#Enemy ------------------------------------------------

enemy_img = []
enemy_x = []
enemy_y = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    img_src = "assets/gps_ufo_" + str(i) + ".png"
    enemy_img.append(pg.image.load(img_src))
    enemy_x.append(random.randint(100,600))
    enemy_y.append(random.randint(50, 100))
    enemyX_change.append(2)
    enemyY_change.append(30) #this control the descending of the enemy when touch the boundaries


# Score -----------------------------------------------

score_value = 0
font = pg.font.Font('freesansbold.ttf', 32)
# Define the position of the score.
textX = 10 
textY = 10

# Define the function to the Score
def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))


# Game Over -------------------------------------------
over_font = pg.font.Font('freesansbold.ttf', 64)


# Define the function to the player
def player(x,y):
    screen.blit(player_img, (x, y))

# Define the function to the enemy
def enemy(x,y,i):
    screen.blit(enemy_img[i], (x, y))

# Define the function to the bullet
def fire_bullet(x,y):
    global bullet_state #make this variable global
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y+10)) #add some pixels to centralize the bullet 

# Define the function to the colicion
def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance=math.sqrt(math.pow(enemy_x-bullet_x,2) + math.pow(enemy_y-bullet_y,2)) #Consult the mathematical formula Distanve between two points and the midpoint
    if distance < 35:  
        return True
    else:
        return False

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Game loop --------------------------------------------------
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
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("assets/laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
                    
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_change = 0
#                print("Up")
    
#   Change the position of the ship        
    player_x += playerX_change

#   Control the boudaries of the screen. the ship cannot p+ass the 0 and the 700        
    if player_x <= 0:
        player_x = 0
    if player_x >= 742:
        player_x = 742    


#   Movments of the enemy and Collision 
    for i in range(num_of_enemies):
        
        print("[i]" + str(i)) 
        print("left enemyX_change[i]" + str(enemyX_change[i]))
        print("left enemy_y[i]" + str(enemy_y[i]))
        
        
        # Game Over
        if enemy_y[i] > 440:

            game_over_text()
            break
        
        
        enemy_x[i] += enemyX_change[i]
#       Control the boudaries of the screen. When the enemy hit the boudaries they change the direction  
        if enemy_x[i] <= 10:
           enemyX_change[i] = 2
           enemy_y[i] += enemyY_change[i]

        elif enemy_x[i] >= 690:
           enemyX_change[i] = -2
           enemy_y[i] += enemyY_change[i]
           

        # Collision
        collision = isCollision(enemy_x[i], enemy_y[i],bullet_x, bullet_y)
        if collision:
            explosionSound = mixer.Sound("assets/explosion.wav")
            explosionSound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 650)
            enemy_y[i] = random.randint(50, 150)

            

#       Call the enemy function
        enemy(enemy_x[i], enemy_y[i], i)    
             
#   Bullet Movment
    if bullet_y < 0:
        bullet_y = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bulletY_change


#   Call the player function
    player(player_x, player_y)    
        
#   Call the player function
    show_score(textX, textY)    

#   to work properly we need to add a update function
    pg.display.update()

