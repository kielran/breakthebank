import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((46, 72))
        self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - 26))
    

        
class JanitorExit(Exit):
    def __init__(self, pos):
        super().__init__(pos)
        self.image.fill('brown')
        
        
class BankerExit(Exit):
    def __init__(self, pos):
        super().__init__(pos)
        self.image.fill('yellow')