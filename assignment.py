import pygame
pygame.init()

Screen_Width = 800
Screen_Height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
background=pygame.image.load("images/road.png")
screen.blit(background,(0,0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
pygame.quit()