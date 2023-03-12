import pygame
from player import Player

class Banker(Player):

    def __init__(self, pos):
        super().__init__(pos)
        #self.image = pygame.Surface((32,64))
        # self.image.fill('red')

    def player_movement(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1

        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()