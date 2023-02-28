import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, distance):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)
        self.posFromStart = 0
        self.speed = 1
        self.distance = distance
        self.direction = 1
    
    def move(self):
        if self.direction == 1:
            self.rect.x += self.speed
            self.posFromStart += self.speed
        elif self.direction == -1:
            self.rect.x -= self.speed
            self.posFromStart -= self.speed
        
    def reverse_dir(self):
        self.direction *= -1
        
    def update(self):
        self.move()
        if self.posFromStart > self.distance or self.posFromStart < 0:
            self.reverse_dir()
        
class Roomba(Enemy):
    def __init__(self, pos, distance, player):
        super().__init__(pos, distance)
        self.sight_image = pygame.Surface((1000, 62))
        self.sight_image.fill((50, 50, 50))
        self.sight_rect = self.sight_image.get_rect(topleft = self.rect.topright)
        self.player = player
        
    def move(self):
        if self.direction == 1:
            self.rect.x += self.speed
            self.sight_rect.x += self.speed
            self.posFromStart += self.speed
        elif self.direction == -1:
            self.rect.x -= self.speed
            self.sight_rect.x -= self.speed
            self.posFromStart -= self.speed
        
    def reverse_dir(self):
        self.direction *= -1
        if self.direction == 1:
            self.sight_rect.topleft = self.rect.topright
        else:
            self.sight_rect.topright = self.rect.topleft
        
    def update(self):
        self.move()
        if self.posFromStart > self.distance or self.posFromStart < 0:
            self.reverse_dir()

        return self.sight_rect
    
    def detect_player(self, player_rect, tiles):
        for tile in tiles.sprites(): #looking through all sprites
            if pygame.Rect.colliderect(self.sight_rect, player_rect): #if enemy collides with sight
                if tile.rect.colliderect(self.sight_rect): #if tile is colliding with the sight
                    #print(player_rect.x < tile.rect.x, tile.rect.x < self.sight_rect.midright[0])
                    if player_rect.x < tile.rect.x and tile.rect.x < self.rect.x:
                        break
                    elif player_rect.x > tile.rect.x and tile.rect.x > self.rect.x:
                        break
                    else: return True
                else:
                    return True
        
        return False