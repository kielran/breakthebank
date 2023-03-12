import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("./imgs/floor1.png"), (46,46)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)