import math
import random
import pygame

screen_width = 800
screen_height = 500
player_startx = 370
player_starty = 380
enemy_startymin = 50
enemy_startymax = 150
enemy_speedx = 4
enemy_speedy = 40
bullet_speedy = 10
hitbox_distance = 27

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load('background.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = player_startx
playerY = player_starty
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemy = 6

for i in range(num_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, screen_width - 64))
    enemyY.append(random.randint(enemy_startymin, enemy_startymax))
    enemyX_change.append(enemy_speedx)
    enemyY_change.append(enemy_speedy)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = player_starty
bulletX_change = 0
bulletY_change = bullet_speedy
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def gameover_text():
    over_text = over_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(over_text, (200, 200))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def coll(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < hitbox_distance

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change