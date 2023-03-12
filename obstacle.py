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
    def __init__(self, pos, size_x, size_y, uniqueID):
        super().__init__()
        self.image = pygame.Surface((size_x, size_y))
        self.image.fill('Red')
        self.rect = self.image.get_rect(bottomleft = pos)
        self.notFlippable = 1
        self.obstacleID = uniqueID
    def __del__(self):
        print('Gone forever')

class InteractBox(pygame.sprite.Sprite):
    def __init__(self, pos, uniqueID):
        super().__init__()
        self.image = pygame.Surface((15, 30))
        self.image.fill('Purple')
        self.rect = self.image.get_rect(topleft = pos)
        self.flipUse = 1
        self.leverID = uniqueID
        self.posNote = pos
    def update(self):
        if self.flipUse == 0: #Currently not working, need to switch images later
            self.image = pygame.Surface((15, 30))
            self.image.fill('Brown')
            self.rect = self.image.get_rect(topleft = self.posNote)