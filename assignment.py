import pygame
pygame.init()
import random

car_y=random.randint(0,50)
car_y1=random.randint(70,100)
Screen_Width = 800
Screen_Height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
lane1_x=9
lane2_x=300
lane3_x=350
lane4_x=400
lanes=[lane1_x,lane2_x, lane3_x, lane4_x]
background=pygame.image.load("images/road.png")
background=pygame.transform.scale(background, (Screen_Width, Screen_Height))
screen.blit(background,(0,0))
bg_speed=5
background_y=0

player_car=pygame.image.load("images/redcar1.png")
player_car=pygame.transform.scale(player_car, (210, 240))
player_x=Screen_Width/2-30
player_y=Screen_Height-150

enemy_car=pygame.image.load("images/enemycar1.png")
enemy_car=pygame.transform.scale(enemy_car, (120, 200))
enemy_car2=pygame.image.load("images/enemycar2.png")
enemy_car2=pygame.transform.scale(enemy_car2, (120, 200))
enemy_car3=pygame.image.load("images/enemycar3.png")
enemy_car3=pygame.transform.scale(enemy_car3, (200, 200))


player_rect=pygame.Rect(370, 450, 60, 120)

enemy1_rect=pygame.Rect(200, -100, 60, 120)
enemy2_rect=pygame.Rect(400, -300, 60, 120)
enemy3_rect=pygame.Rect(600, -500, 60, 120)

bg_y=0
bg_speed=5
enemy_speed=5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    bg_y+=bg_speed
    if bg_y>Screen_Height:
        bg_y=0
    screen.blit(background, (0,bg_y - Screen_Height))
    screen.blit(background, (0, bg_y))

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x>0:
        player_rect.x -=7
    if keys[pygame.K_RIGHT] and player_rect.x<Screen_Width-player_rect.width:
       player_rect.x+=7

    enemy1_rect.y+=enemy_speed
    enemy2_rect.y+=enemy_speed
    enemy3_rect.y+=enemy_speed

    if enemy1_rect.y> Screen_Height:
        enemy1_rect.y=random.randint(-600,-100)
        enemy1_rect.x=random.choice(lanes)
    if enemy2_rect.y>Screen_Height:
        enemy2_rect.y=random.randint(-600, -100)
        enemy2_rect.x=random.choice(lanes)
    if enemy3_rect.y>Screen_Height:
        enemy3_rect.y=random.randint(-600,-100)
        enemy3_rect.x=random.choice(lanes)
    screen.blit(enemy_car,(enemy1_rect.x, enemy1_rect.y))
    screen.blit(enemy_car2, (enemy2_rect.x, enemy2_rect.y))
    screen.blit(enemy_car3, (enemy3_rect.x, enemy3_rect.y))

    screen.blit(player_car,(player_rect.x, player_rect.y))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()