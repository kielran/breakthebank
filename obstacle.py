import pygame


class PointObstacle(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image = pygame.image.load("./imgs/coin.png")
        #self.image.fill('Blue')
        self.rect = self.image.get_rect(topleft = pos)
    def __del__(self):
        # print('Point deletion')
        pass

class InteractObstacle(pygame.sprite.Sprite):
    def __init__(self, pos, size_x, size_y, uniqueID):
        super().__init__()
        if uniqueID == 0:
            self.image = pygame.Surface((size_x, size_y))
            self.image.fill('Pink')
            self.rect = self.image.get_rect(bottomleft = pos)
        else: 
            #self.image = pygame.Surface((size_x, size_y))
            #self.image.fill('Red')
            self.image = pygame.transform.scale(pygame.image.load("./imgs/floor2.png"), (size_x,size_y)).convert_alpha()
            self.rect = self.image.get_rect(bottomleft = pos)
        self.obstacleID = uniqueID
    def __del__(self):
        # print('Gone forever')
        pass

class InteractBox(pygame.sprite.Sprite):
    def __init__(self, pos, uniqueID):
        super().__init__()
        self.image = pygame.Surface((19, 28))
        self.image = pygame.image.load("./imgs/leverup.png")
        #self.image.fill('Purple')
        self.rect = self.image.get_rect(topleft = pos)
        self.flipUse = 1
        self.leverID = uniqueID
        self.posNote = pos
    def update(self):
        if self.flipUse == 0: #Currently not working, need to switch images later
            self.image = pygame.Surface((15, 30))
            self.image = pygame.image.load("./imgs/leverdown.png")
            #self.image.fill('Brown')
            self.rect = self.image.get_rect(topleft = self.posNote)
