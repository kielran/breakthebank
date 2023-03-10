import pygame


class PointObstacle(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('Blue')
        self.rect = self.image.get_rect(topleft = pos)
    def __del__(self):
        print('Point deletion')

class InteractObstacle(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('Red')
        self.rect = self.image.get_rect(topleft = pos)
    def __del__(self):
        print('Gone forever')

class InteractBox(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__
        self.image = pygame.Surface((size, size))
        self.image.fill('Purple')
        self.rect = self.image.get_rect(topleft = pos)
        self.interactable = InteractObstacle(pos, size)