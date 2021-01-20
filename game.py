# NOTICE: Lines marked with the hashtag (#) symbol are comments. They provide a description of what the code block does. They do not affect the actual code.


# Importing modules for our game
import pygame
import random
import os
import time
import math
from pygame import mixer
import sys

# Changes the current working directory so we can directly import images instead of having to copy path
path = "C:/Users/rahul/Desktop/test/PersonalProject/images"
os.chdir(path)

# Initializes the game, and creates the window
pygame.init()
screen = pygame.display.set_mode((1280, 800))

# Background Image
bg = pygame.image.load('bg.jpg')


# Sets the window title and logo
pygame.display.set_caption('Rahul Vikram Grade 10 - Per. 2 MYP Personal Project')
icon = pygame.image.load('gameicon.png')
pygame.display.set_icon(icon)

# Creates the player
playerimg = pygame.image.load('spaceship.png')
playerX = 560
playerY = 650
playerX_change = 0

# Creates the bullet
# start = bullet is invisible
# inmotion = bullet is moving
itemimg = pygame.image.load('item.png')
itemX = 0
itemY = playerY
itemX_change = 0
itemY_change = 3.2
itemstate = 'start'

# Multiple enemy creation
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_count = 8

# Creates the enemy
for i in range(enemy_count):
    enemyimg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 1100))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(1.78)
    enemyY_change.append(50)

# score creation
score_val = 0
font = pygame.font.Font('freesansbold.ttf', 40)

posY1 = 15
posX1 = 15

gameoverfont = pygame.font.Font('freesansbold.ttf', 128)

def gameover():
    gmovrtext = gameoverfont.render("GAME OVER", True, (255,255,255))
    screen.blit(gmovrtext, (200, 350))

# Changes the working directory in order to access sound effects
path2 = "C:/Users/rahul/Desktop/test/PersonalProject/sound"
os.chdir(path2)


def printscore1(x, y):
    score = font.render(f"Score: {str(score_val)}", True, (255,255,255))
    screen.blit(score,(x, y))

posY2 = 17
posX2 = 17
def printscore2(x, y):
    score = font.render(f"Score: {str(score_val)}", True, (0,0,0))
    screen.blit(score,(x, y))


# Displays the player on screen
def player(x, y):
    screen.blit(playerimg,(x, y))

# Displays the enemy on screen
def enemy(x, y, i):
    screen.blit(enemyimg[i],(x, y))

# Displays bullet on screen
def startbullet(x, y):
    global itemstate
    itemstate = 'inmotion'
    screen.blit(itemimg, (x + 32, y - 17))


def ifcollision(enemyX,enemyY,itemX,itemY):
    # math. references the math module which was imported at the top
    # math.sqrt: square root

    # distance function
    dist = math.sqrt(
        # math.pow: math power function
        (math.pow(enemyX-itemX,2)) + (math.pow(enemyY-itemY,2))
        )
    
    if dist < 56:
        return True
    else:
        return False


# Keeps the pygame window running, but adds an event loop so it doesn't return an error message.
running = True
while running:
    # Sets the background Color (RGB)
    screen.fill((0, 0, 0))
    # Loading in Background Image
    screen.blit(bg,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed
        if event.type == pygame.KEYDOWN:
            print('Keystroke is pressed.')

            # Checks which keystroke is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            if event.key == pygame.K_SPACE:

                # Makes it so the current onscreen bullet has to exit the screen before another one can be fired
                if itemstate == 'start':
                    itemsfx = mixer.Sound('lasersfx.wav')
                    itemsfx.play()
                    itemX = playerX
                    startbullet(playerX, itemY)


        # If keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0


    # Updates the position of the ship based on keystrokes
    # Adds screen boundaries so that the player does not go off screen
    playerX += playerX_change

    # Moving the player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1153:
        playerX = 1153

    if playerY <= 350:
        playerY = 350
    elif playerY >= 672:
        playerY = 672

    # Moving bullets
    if itemY <= 0:
        itemY = 650
        itemstate = 'start'

    if itemstate == 'inmotion':
        startbullet(itemX, itemY)
        itemY -= itemY_change


    # Moving the enemy
    for i in range(enemy_count):
        if enemyY[i] > 600:
            for j in range(enemy_count):
                enemyY[j] == 4500

            gameover()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.78
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1153:
            enemyX_change[i] = -1.78
            enemyY[i] += enemyY_change[i]


        # assigns collision variable to the collision function defined on line 64
        collision = ifcollision(enemyX[i], enemyY[i], itemX, itemY)

        # checks if the collision() function returned True or False
        if collision:
            contactsound = mixer.Sound('enemysfx.wav')
            contactsound.play()
            itemY = 650
            itemstate = 'start'
            score_val += 1
            # respawns the enemy if collision() returns True
            enemyX[i] = random.randint(0, 1100)
            enemyY[i] = random.randint(0, 50)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    printscore2(posX2, posY2)
    printscore1(posX1, posY1)
    pygame.display.update()
