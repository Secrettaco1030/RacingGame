import pygame
pygame.init()
import random

car_y=random.randint(0,50)
car_y1=random.randint(70,100)
Screen_Width = 800
Screen_Height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
lane1_x=200
lane2_x=310
lane3_x=460
lane4_x=590
lanes=[lane1_x,lane2_x, lane3_x, lane4_x]
background=pygame.image.load("images/road.png")
background=pygame.transform.scale(background, (Screen_Width, Screen_Height))
screen.blit(background,(0,0))
bg_speed=5
background_y=0

player_car=pygame.image.load("images/redcar1.png")
player_car=pygame.transform.scale(player_car, (120, 200))
player_x=Screen_Width/2-30
player_y=Screen_Height-150

enemy_car=pygame.image.load("images/enemycar1.png")
enemy_car=pygame.transform.scale(enemy_car, (100, 180))
enemy_car2=pygame.image.load("images/enemycar2.png")
enemy_car2=pygame.transform.scale(enemy_car2, (100, 180))
enemy_car3=pygame.image.load("images/enemycar3.png")
enemy_car3=pygame.transform.scale(enemy_car3, (110, 180))


player_rect=player_car.get_rect()
player_rect.centerx = Screen_Width // 2
player_rect.bottom = Screen_Height - 20
enemy1_rect=enemy_car.get_rect()
enemy2_rect=enemy_car2.get_rect()
enemy3_rect=enemy_car3.get_rect()

enemy1_rect.y = random.randint(-600, -100)
enemy1_rect.centerx = random.choice(lanes)
enemy2_rect.y = random.randint(-600, -100)
enemy2_rect.centerx = random.choice(lanes)
enemy3_rect.y = random.randint(-600, -100)
enemy3_rect.centerx = random.choice(lanes)
bg_y=0
bg_speed=5
enemy_speed=5
game_over=False
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
        if keys[pygame.K_LEFT] and player_rect.left>0:
            player_rect.x -=7
        if keys[pygame.K_RIGHT] and player_rect.right<Screen_Width:
            player_rect.x+=7
        if keys[pygame.K_UP] and player_rect.y>0:
            player_rect.y -=7
        if keys[pygame.K_DOWN] and player_rect.y<Screen_Height:
            player_rect.y +=7
        if not game_over:
            enemy1_rect.y+=enemy_speed
            enemy2_rect.y+=enemy_speed
            enemy3_rect.y+=enemy_speed

        if enemy1_rect.y> Screen_Height:
            enemy1_rect.y=random.randint(-600,-100)
            enemy1_rect.centerx=random.choice(lanes)
        if enemy2_rect.y>Screen_Height:
            enemy2_rect.y=random.randint(-600, -100)
            enemy2_rect.centerx=random.choice(lanes)
        if enemy3_rect.y>Screen_Height:
            enemy3_rect.y=random.randint(-600,-100)
            enemy3_rect.centerx=random.choice(lanes)

        screen.blit(enemy_car,(enemy1_rect.x, enemy1_rect.y))
        screen.blit(enemy_car2, (enemy2_rect.x, enemy2_rect.y))
        screen.blit(enemy_car3, (enemy3_rect.x, enemy3_rect.y))
        screen.blit(player_car,(player_rect.x, player_rect.y))
        
        if (player_rect.colliderect(enemy1_rect) or
            player_rect.colliderect(enemy2_rect) or
            player_rect.colliderect(enemy3_rect)):
            game_over=True
            bg_speed=0
            enemy_speed=0

        screen.blit(player_car,(player_rect.x, player_rect.y))

        if game_over:
            font = pygame.font.SysFont('Arial', 80)
            text=font.render("GAME OVER", True, (255,0,0))
            screen.blit(text,(Screen_Width//2-text.get_width()//2,250))
        pygame.display.flip()
        clock.tick(60)

pygame.quit()