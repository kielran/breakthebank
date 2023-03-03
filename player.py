import pygame
from item import Item, JanitorItem, BankerItem


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill("pink")
        self.rect = self.image.get_rect(topleft = pos)
        
        #player movement
        
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -16
        self.inventory = []

    def player_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        
    def pick_up_item(self, items):
        for item in items.sprites():
            if self.rect.colliderect(item.rect) and len(self.inventory) < 1 and ((type(self) == Banker and type(item) == BankerItem) or (type(self) == Janitor and type(item) == JanitorItem)):
                self.inventory.append(item)
                item.collect_item(self.rect.center)
    
    def drop_item(self):
        if len(self.inventory) > 0:
            self.inventory[0].drop_item(self.rect.topleft)
            self.inventory.clear()
    


    def update(self, items):
        self.player_movement()
        keys = pygame.key.get_pressed()
        
        if (len(self.inventory)) > 0:
            self.inventory[0].update(self.rect.center, self.direction.x)

        if keys[pygame.K_k]:
            self.pick_up_item(items)
        if keys[pygame.K_j]:
            self.drop_item()
        self.rect.x += self.direction.x * self.speed
        
class Janitor(Player):
    def __init__(self, pos):
        super().__init__(pos)
        
class Banker(Player):
    def __init__(self, pos):
        super().__init__(pos)