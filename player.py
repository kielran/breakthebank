import pygame
from item import Item, JanitorItem, BankerItem


bankerr1 = pygame.image.load('imgs/banker_sprite/banker_walk/r1.png'); bankerr2 = pygame.image.load('imgs/banker_sprite/banker_walk/r2.png'); bankerr3 = pygame.image.load('imgs/banker_sprite/banker_walk/r3.png'); bankerr4 = pygame.image.load('imgs/banker_sprite/banker_walk/r4.png')
bankerr5 = pygame.image.load('imgs/banker_sprite/banker_walk/r5.png')
bankerr6 = pygame.image.load('imgs/banker_sprite/banker_walk/r6.png')
bankerr7 = pygame.image.load('imgs/banker_sprite/banker_walk/r7.png')
bankerright = []
bankerright.append(bankerr1), bankerright.append(bankerr2), bankerright.append(bankerr3), bankerright.append(bankerr4)
bankerright.append(bankerr5)
bankerright.append(bankerr6)
bankerright.append(bankerr7)

for banker in bankerright:
    pygame.transform.scale_by(banker, 0.1)
bankerl1 = pygame.image.load('imgs/banker_sprite/banker_walk/l1.png')
bankerl2 = pygame.image.load('imgs/banker_sprite/banker_walk/l2.png')
bankerl3 = pygame.image.load('imgs/banker_sprite/banker_walk/l3.png')
bankerl4 = pygame.image.load('imgs/banker_sprite/banker_walk/l4.png')
bankerl5 = pygame.image.load('imgs/banker_sprite/banker_walk/l5.png')
bankerl6 = pygame.image.load('imgs/banker_sprite/banker_walk/l6.png')
bankerl7 = pygame.image.load('imgs/banker_sprite/banker_walk/l7.png')
bankerleft = []
bankerleft.append(bankerl1), bankerleft.append(bankerl2), bankerleft.append(bankerl3), bankerleft.append(bankerl4)
bankerleft.append(bankerl5)
bankerleft.append(bankerl6)
bankerleft.append(bankerl7)
# for banker in bankerleft:
#     banker = pygame.transform.scale_by(banker, 0.1).convert_alpha()
#     print("hi")
for index, banker in enumerate(bankerright):
    bankerright[index] = pygame.transform.scale_by(banker, 0.72)
for index, banker in enumerate(bankerleft):
    bankerleft[index] = pygame.transform.scale_by(banker, 0.72)
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = bankerright[0]
        self.rect = self.image.get_rect(topleft = pos)
        #player movement
        
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -16
        self.inventory = []
        self.counter = 0
        self.facingRight = True

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.image = bankerright[self.counter]
            self.counter = (self.counter + 1) % len(bankerright)
            self.direction.x = 1
            self.facingRight = True
        elif keys[pygame.K_a]:
            self.image = bankerleft[self.counter]
            self.counter = (self.counter + 1) % len(bankerleft)
            self.direction.x = -1
            self.facingRight = False
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
            self.inventory[0].update(self.rect.center, self.facingRight)

        if keys[pygame.K_s]:
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