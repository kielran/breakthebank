import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft = pos)
        self.collected = False
        self.gravity = 0.8
        
    def collect_item(self):
        self.collected = True   
    
    def drop_item(self, pos):
        self.collected = False
        self.rect.topleft = pos

        
class JanitorItem(Item):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image.fill("brown")
        
        
class BankerItem(Item):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image.fill("yellow")
        
        