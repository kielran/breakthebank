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

janitorr1 = pygame.image.load('imgs/janitor_sprite/janitor_walk/r1.png'); janitorr2 = pygame.image.load('imgs/janitor_sprite/janitor_walk/r2.png'); janitorr3 = pygame.image.load('imgs/janitor_sprite/janitor_walk/r3.png'); janitorr4 = pygame.image.load('imgs/janitor_sprite/janitor_walk/r4.png')
janitorr5 = pygame.image.load('imgs/janitor_sprite/janitor_walk/r5.png')
janitorr6 = pygame.image.load('imgs/janitor_sprite/janitor_walk/r6.png')
janitorr7 = pygame.image.load('imgs/janitor_sprite/janitor_walk/r7.png')
janitorright = []
janitorright.append(janitorr1), janitorright.append(janitorr2), janitorright.append(janitorr3), janitorright.append(janitorr4)
janitorright.append(janitorr5)
janitorright.append(janitorr6)
janitorright.append(janitorr7)

janitorl1 = pygame.image.load('imgs/janitor_sprite/janitor_walk/l1.png')
janitorl2 = pygame.image.load('imgs/janitor_sprite/janitor_walk/l2.png')
janitorl3 = pygame.image.load('imgs/janitor_sprite/janitor_walk/l3.png')
janitorl4 = pygame.image.load('imgs/janitor_sprite/janitor_walk/l4.png')
janitorl5 = pygame.image.load('imgs/janitor_sprite/janitor_walk/l5.png')
janitorl6 = pygame.image.load('imgs/janitor_sprite/janitor_walk/l6.png')
janitorl7 = pygame.image.load('imgs/janitor_sprite/janitor_walk/l7.png')
janitorleft = []
janitorleft.append(janitorl1), janitorleft.append(janitorl2), janitorleft.append(janitorl3), janitorleft.append(janitorl4)
janitorleft.append(janitorl5)
janitorleft.append(janitorl6)
janitorleft.append(janitorl7)

for index, banker in enumerate(bankerright):
    bankerright[index] = pygame.transform.scale_by(banker, 0.48)
for index, banker in enumerate(bankerleft):
    bankerleft[index] = pygame.transform.scale_by(banker, 0.48)
    
for index, janitor in enumerate(janitorright):
    janitorright[index] = pygame.transform.scale_by(janitor, 0.48)
for index, janitor in enumerate(janitorleft):
    janitorleft[index] = pygame.transform.scale_by(janitor, 0.48)
    
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = bankerright[0]
        self.rect = self.image.get_rect(topleft = pos)
        #player movement
        
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -13
        self.inventory = []
        self.counter = 0
        self.facingRight = True
        self.canMove = True

        self.is_on_ground = False

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

        if keys[pygame.K_w] and self.is_on_ground == True:
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

        if keys[pygame.K_f]:
            self.pick_up_item(items)
        if keys[pygame.K_j]:
            self.drop_item()
        self.rect.x += self.direction.x * self.speed
        
class Janitor(Player):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = janitorright[0]
        self.rect = self.image.get_rect(topleft = pos)
        
    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.canMove:
            self.image = janitorright[self.counter]
            self.counter = (self.counter + 1) % len(janitorright)
            self.direction.x = 1
            self.facingRight = True
        elif keys[pygame.K_a] and self.canMove:
            self.image = janitorleft[self.counter]
            self.counter = (self.counter + 1) % len(janitorleft)
            self.direction.x = -1
            self.facingRight = False
        else:
            self.direction.x = 0

        if keys[pygame.K_w] and self.is_on_ground and self.canMove:
            self.jump()
            
    def update(self, items, water, tiles):
        self.player_movement()
        keys = pygame.key.get_pressed()
        
        if (len(self.inventory)) > 0:
            self.inventory[0].update(self.rect.center, self.facingRight)

        if keys[pygame.K_f]:
            self.pick_up_item(items)
        if keys[pygame.K_j]:
            self.drop_item()
        if keys[pygame.K_c] and len(self.inventory) > 0:
            self.clean_water(water, tiles)

        self.rect.x += self.direction.x * self.speed
    
    def clean_water(self, waterObjects, tiles):
        for waterObject in waterObjects:
            for waterTile in waterObject.tiles.sprites():
                if waterTile.rect.midtop[1] == self.rect.midbottom[1] and waterObject.startX <= self.rect.midbottom[0] and waterObject.endX >= self.rect.midbottom[0]:
                    waterObject.clean(tiles)
                
class Banker(Player):

    def __init__(self, pos):
        super().__init__(pos)
        #self.image = pygame.Surface((32,64))
        # self.image.fill('red')

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.canMove:
            self.image = bankerright[self.counter]
            self.counter = (self.counter + 1) % len(bankerright)
            self.direction.x = 1
            self.facingRight = True
        elif keys[pygame.K_LEFT] and self.canMove:
            self.image = bankerleft[self.counter]
            self.counter = (self.counter + 1) % len(bankerleft)
            self.direction.x = -1
            self.facingRight = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.is_on_ground == True and self.canMove:
            self.jump()
            
    def update(self, items, elevators, janitor):
        self.player_movement()
        keys = pygame.key.get_pressed()
        
        if (len(self.inventory)) > 0:
            self.inventory[0].update(self.rect.center, self.facingRight)

        if keys[pygame.K_f]:
            self.pick_up_item(items)
        if keys[pygame.K_j]:
            self.drop_item()
        if keys[pygame.K_DOWN] and len(self.inventory) > 0:
            self.activate_elevator(elevators, janitor)

        self.rect.x += self.direction.x * self.speed
        
    def activate_elevator(self, elevators, janitor):
        for elevator in elevators:
            print("elevator")
            if self.rect.midbottom[1] == elevator.rect.midtop[1] and elevator.startX <= self.rect.midbottom[0] and elevator.endX >= self.rect.midbottom[0]:
                print("on elevator")
                self.canMove = False
                if janitor.rect.midbottom[1] == elevator.rect.midtop[1] and elevator.startX <= janitor.rect.midbottom[0] and elevator.endX >= janitor.rect.midbottom[0]:
                    janitor.canMove = False
                elevator.activate()
                
    
