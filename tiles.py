import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)