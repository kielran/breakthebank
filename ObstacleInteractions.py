import pygame
import sys
import os
from sys import exit

pygame.init();
gravity = 10
moveDirection = 10

if not os.path.exists("imgs"):
    print("you do not have imgs folder")

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,30))
        self.image.fill('Green')
        self.rect = self.image.get_rect(topleft = (700,300))
        pygame.draw.rect(screen, 'Green', self.rect)
    def __del__(self):
        print('No more')
    def update(self):
        pygame.draw.rect(screen, 'Green', self.rect)
    

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((20,30))
        self.image.fill('Blue')
        self.rect = self.image.get_rect(topleft = (100,300))
        self.rect = self.image.get_rect()
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if self.rect.bottom >= 400: 
            self.rect.bottom = 400
        pygame.draw.rect(screen, 'Blue', self.rect)


player_list = pygame.sprite.Group()
obstacle_list = pygame.sprite.Group()

bankerPlayer = Player(20, 30)
bankerPlayer.rect.x = 50
bankerPlayer.rect.y = 300
player_list.add(bankerPlayer)

obstacleTest = Obstacle()
obstacle_list.add(obstacleTest)
# janitorPlay = Player()
# player_list.add(janitorPlay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                for obstacle in obstacle_list:
                    if bankerPlayer.rect.colliderect(obstacle.rect):
                        obstacle.kill()
                        del obstacle
                        print('Collision detected')
    

    player_list.update()
    obstacle_list.update()

    screen.fill('Black')
    obstacle_list.draw(screen)
    player_list.draw(screen)
    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)