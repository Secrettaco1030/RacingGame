import pygame
pygame.init()
import random

score=0
#https://www.pygame.org/docs/ref/rect.html#pygame.Rect.inflate_ip
#pygame.mixer.music.load("sounds/gamemusic.mp3")
#pygame.mixer.music.play(-1)
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
home_button=pygame.image.load("images/homebutton2.jpg")
home_button=pygame.transform.scale(home_button, (100, 100))

background=pygame.transform.scale(background, (Screen_Width, Screen_Height))
screen.blit(background,(0,0))
bg_speed=5
background_y=0
Light_grey=(112, 108, 97)
restart_button=pygame.Rect(250,450,300,70)
score_counter=pygame.Rect(670,65,100,50)
score_font = pygame.font.Font("Fonts/TheScoreRegular-ywdy3.otf", 40)
font_color=(252, 191, 73)
font1=pygame.font.Font("Fonts/GamepauseddemoRegular-RpmY6.otf",150)
font=pygame.font.SysFont("Arial", 30)

player_car=pygame.image.load("images/redcar1.png")
player_car=pygame.transform.scale(player_car, (120, 200))
player_x=Screen_Width/2-30
player_y=Screen_Height-150
player_hitbox=pygame.Rect(0,0,90,160)


enemy_car=pygame.image.load("images/enemycar1.png")
enemy_car=pygame.transform.scale(enemy_car, (100, 180))
enemy_carbox=pygame.image.load("images/enemycar1.png")
enemy_carbox=pygame.transform.scale(enemy_carbox,(90,90))
enemy_car2=pygame.image.load("images/enemycar2.png")
enemy_car2=pygame.transform.scale(enemy_car2, (100, 180))
enemy_car3=pygame.image.load("images/enemycar3.png")
enemy_car3=pygame.transform.scale(enemy_car3, (110, 180))


player_rect=player_car.get_rect()
player_rect.inflate_ip(-40,-40)
player_rect.centerx = (Screen_Width // 2)
player_rect.bottom = Screen_Height


enemy1_rect=enemy_car.get_rect()
#enemy1_rect.inflate_ip(-20,-40)
enemy2_rect=enemy_car2.get_rect()
#enemy2_rect.inflate_ip(-20,-40)
enemy3_rect=enemy_car3.get_rect()
#enemy3_rect.inflate_ip(-20,-40)




enemy1_rect.y = random.randint(-600, -100)
enemy2_rect.y = random.randint(-600, -100)
enemy3_rect.y = random.randint(-600, -100)

spawn_lane=random.sample(lanes,3)
enemy1_rect.centerx = spawn_lane[0]
enemy2_rect.centerx = spawn_lane[1]
enemy3_rect.centerx = spawn_lane[2]

bg_y=0
bg_speed=5
enemy_speed=5
game_over=False
running = True

while running:
        mousepressed=False
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepressed=True
        if game_over and mousepressed:
            if restart_button.collidepoint(mouseX, mouseY):
                game_over=False
                bg_speed=5
                enemy_speed=5
                score=0
                player_rect.centerx = Screen_Width // 2
                player_rect.bottom = Screen_Height

                # Reset enemy positions and lanes
                spawn_lane = random.sample(lanes, 3)
                enemy1_rect.y = random.randint(-600, -100)
                enemy2_rect.y = random.randint(-600, -100)
                enemy3_rect.y = random.randint(-600, -100)

                enemy1_rect.centerx = spawn_lane[0]
                enemy2_rect.centerx = spawn_lane[1]
                enemy3_rect.centerx = spawn_lane[2]

        bg_y+=bg_speed
        if bg_y>Screen_Height:
            bg_y=0
        screen.blit(background, (0,bg_y - Screen_Height))
        screen.blit(background, (0, bg_y))

        keys=pygame.key.get_pressed()

        score +=1/30

        if keys[pygame.K_LEFT] and player_x>0:
            player_x -=7
            player_y-=3
        if keys[pygame.K_RIGHT] and player_x<Screen_Width-120:
            player_x+=7
            player_y-=3
        if keys[pygame.K_UP] and player_y>0:
            player_y -=7
        if keys[pygame.K_DOWN] and player_y<Screen_Height-200:
            player_y +=7
        player_hitbox.center=(player_x+60, player_y+100)

        if not game_over:
            enemy1_rect.y+=enemy_speed
            enemy2_rect.y+=enemy_speed
            enemy3_rect.y+=enemy_speed

        if (enemy1_rect.y> Screen_Height or
            enemy2_rect.y > Screen_Height or
            enemy3_rect.y > Screen_Height):
            spawn_lane=random.sample(lanes,3)
            enemy1_rect.y=random.randint(-600, -100)

            enemy2_rect.y=random.randint(-600, -100)
            enemy3_rect.y=random.randint(-600, -100)
            enemy1_rect.centerx=spawn_lane[0]
            enemy2_rect.centerx=spawn_lane[1]
            enemy3_rect.centerx=spawn_lane[2]




        screen.blit(enemy_car,(enemy1_rect.x, enemy1_rect.y))
        screen.blit(enemy_car2, (enemy2_rect.x, enemy2_rect.y))
        screen.blit(enemy_car3, (enemy3_rect.x, enemy3_rect.y))
        screen.blit(home_button, (20,20))

        pygame.draw.rect(screen,Light_grey, score_counter)
        score_text=score_font.render(str(round(score)), True, (255,0,0))
        screen.blit(score_text,(700,64))

        #pygame.draw.rect(screen, (255, 0, 0), enemy1_rect, 2)
        #pygame.draw.rect(screen, (0, 255, 0), enemy2_rect, 2)
        #pygame.draw.rect(screen, (0, 0, 255), enemy3_rect, 2)


        if (player_hitbox.colliderect(enemy1_rect) or
            player_hitbox.colliderect(enemy2_rect) or
            player_hitbox.colliderect(enemy3_rect)):
            game_over=True
            bg_speed=0
            enemy_speed=0

        screen.blit(player_car,(player_x, player_y))



        if game_over:
            font = pygame.font.SysFont('Arial', 80)
            font2=pygame.font.SysFont('Arial', 70)
            text=font1.render("GAME OVER", True, (255,0,0))
            screen.blit(text,(Screen_Width//2-text.get_width()//2,250))
            pygame.draw.rect(screen,Light_grey, restart_button)
            screen.blit(font2.render("Restart", True,font_color ),(280,445))
            


        pygame.display.flip()
        clock.tick(60)


pygame.quit()