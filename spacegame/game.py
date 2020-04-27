import pygame
import math
from pygame import mixer

# initilise pygame
pygame.init()

# set screen
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('868.jpg')
background = pygame.transform.scale(background, (800, 600))

#backmusic
mixer.music.load('background.wav')
mixer.music.play(-1)

# set title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('874.jpg')
icon = pygame.transform.scale(icon, (45, 45))

pygame.display.set_icon(icon)

#blast image
blastimg = pygame.image.load("711.jpg")
blastimg = pygame.transform.scale(blastimg,(100,100))
# player ship
playerimg = pygame.image.load("310.jpg")
playerimg = pygame.transform.scale(playerimg, (200, 200))
playerX = 300
playerY = 450
dx = 0

#enemyship
enemyimg = pygame.image.load("691.jpg")
enemyimg = pygame.transform.scale(enemyimg, (100, 100))
enemyX = 0
enemyY = 10
enemy2X = 110
enemy2Y = 10
enemy3X= 210
enemy3Y = 10
endx = 7

# bullet
bulletimg = pygame.image.load("567.jpg")
bulletimg = pygame.transform.scale(bulletimg, (32, 32))
bulletX = 0
bulletY = 450
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready"
#score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 40
textY = 10

#game over
game_font = pygame.font.Font('freesansbold.ttf',64)

def over():
    OVER_TEXT = game_font.render("GAME OVER",True,(255,0,0))
    screen.blit(OVER_TEXT, (200, 200))

def show_score(x,y):
    scores = font.render("Score :" + str(score),True,(0,255,0))
    screen.blit(scores, (x, y))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y):
    screen.blit(enemyimg, (x, y))

def blast(x,y):
    screen.blit(blastimg,(x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 90, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# game loop
running = True
while running:

    # screen color
    screen.fill((0, 0, 0))
    # background img
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -6
            if event.key == pygame.K_RIGHT:
                dx = 6
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0

    playerX += dx
    #enemy movement
    enemyX += endx
    if enemyX >= 570:
        enemyX = 0
        enemyY += 50
    enemy2X += endx
    if enemy2X >= 670:
        enemy2X = 10
        enemy2Y += 50
    enemy3X += endx
    if enemy3X >= 700:
        enemy3X = 30
        enemy3Y += 50

#GAME OVER

    #player movement
    if playerX < 0:
        playerX = 0
    elif playerX > 600:
        playerX = 600
    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    collision2 = isCollision(enemy2X, enemy2Y, bulletX, bulletY)
    collision3 = isCollision(enemy2X, enemy2Y, bulletX, bulletY)

    if collision:
        exp_sound = mixer.Sound('explosion.wav')
        exp_sound.play()
        bulletY = 480
        bullet_state = "ready"
        blast(enemyX, enemyY)
        score += 1
        enemyX = 0
        enemyY = 10

    if collision2:
        exp_sound = mixer.Sound('explosion.wav')
        exp_sound.play()
        bulletY = 480
        bullet_state = "ready"
        blast(enemy2X, enemy2Y)
        score +=1
        enemy2X = 0
        enemy2Y = 10

    if collision3:
        exp_sound = mixer.Sound('explosion.wav')
        exp_sound.play()
        bulletY = 480
        bullet_state = "ready"
        blast(enemy3X, enemy3Y)
        score += 1
        enemy3X = 0
        enemy3Y = 10

    if enemyY >= 450 or enemy2Y >= 450 or enemy3Y >= 450:
        over()

    enemy(enemyX,enemyY)
    enemy(enemy2X, enemy2Y)
    enemy(enemy3X, enemy3Y)
    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
