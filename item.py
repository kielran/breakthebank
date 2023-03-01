import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.uncollected_image = pygame.Surface(size)
        self.collected_image = pygame.Surface((size[0]/2.5, size[1]/2.5))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.collected = False
        self.gravity = 0.4
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
        
    def collect_item(self, pos):
        self.collected = True   
        self.image = self.collected_image
        self.rect = self.image.get_rect(topright = pos)
        self.gravity = 0
    
    def drop_item(self, pos):
        self.collected = False
        self.image = self.uncollected_image
        self.rect = self.image.get_rect(topleft = pos)
        self.gravity = 0.4
        
    def update(self, pos, direction):
        if direction >= 0:
            self.rect.topright = pos
        else:
            self.rect.topleft = pos
        
            

        
class JanitorItem(Item):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image.fill("brown")
        
        
class BankerItem(Item):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image.fill("yellow")
        
        