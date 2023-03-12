import pygame

#when player enters elevator and activates it, they cannot move until the elevator stops moving
class Elevator(pygame.sprite.Sprite):
    def __init__(self, pos, distance, speed):
        super().__init__()
        self.image = pygame.Surface((100, 23))
        self.image.fill("black")
        self.rect = self.image.get_rect(topleft = pos)
        self.distance = distance
        self.posFromStart = 0
        self.direction = 1
        self.speed = speed
        self.activated = False
        self.startX = pos[0]
        self.endX = self.startX + 100
        
    def move(self):
        if self.direction == 1:
            self.rect.y -= self.speed
            self.posFromStart += self.speed
        elif self.direction == -1:
            self.rect.y += self.speed
            self.posFromStart -= self.speed
        
    def reverse_dir(self):
        self.direction *= -1
        
    def activate(self):
        self.activated = True
        
    def update(self, banker, janitor):
        if self.activated:
            self.move()
            if self.posFromStart > self.distance or self.posFromStart < 0:
                self.reverse_dir()
                self.activated = False
                print(banker, janitor)
                banker.canMove = True
                janitor.canMove = True
                