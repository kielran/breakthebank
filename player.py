import pygame

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
        self.counter = 0

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.image = bankerright[self.counter]
            self.counter = (self.counter + 1) % len(bankerright)
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.image = bankerleft[self.counter]
            self.counter = (self.counter + 1) % len(bankerleft)
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


    def update(self):
        self.player_movement()
        self.rect.x += self.direction.x * self.speed