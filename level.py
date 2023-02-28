import pygame
from tiles import Tile
from player import Player
from enemy import Roomba
from item import JanitorItem, BankerItem

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        tile_size = 64
        for row_index, row in enumerate(layout):
            # print(row_index)
            # print(row)

            for col_index, cell in enumerate(row):
                #print(f'{row_index},{col_index}:{cell}')
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == "X":    
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                    
                if cell == "E":
                    roomba_sprite = Roomba((x, y), 300, self.player)
                    self.enemies.add(roomba_sprite)
                
                if cell == "J":
                    janitor_item_sprite = JanitorItem((x, y), (64, 32))
                    self.items.add(janitor_item_sprite)
                
                if cell == "B":
                    banker_item_sprite = BankerItem((x, y), (64, 32))
                    self.items.add(banker_item_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite  
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(player.rect): #if player collides with a tile
                if player.direction.x < 0: #moving left
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: #moving right
                    player.rect.right = sprite.rect.left
                

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for item in self.items:
            item.apply_gravity()
        

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(player.rect): #if player collides with a tile
                
                if player.direction.y > 0: #moving left
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

                elif player.direction.y < 0: #moving right
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
            for item in self.items.sprites():
                if sprite.rect.colliderect(item.rect): #if player collides with a tile
                
                    if item.direction.y > 0: #moving left
                        item.rect.bottom = sprite.rect.top
                        item.direction.y = 0

                    elif item.direction.y < 0: #moving right
                        item.rect.top = sprite.rect.bottom
                        item.direction.y = 0
                    

    def run(self):
        self.tiles.draw(self.display_surface)
        
        for enemy in self.enemies:
            sight_rect = enemy.update()
            pygame.draw.rect(self.display_surface, "white", sight_rect)   #comment out to not draw the sight rect
            for player in self.player:
                if enemy.detect_player(player.rect, self.tiles):
                    print("detected")
        self.enemies.draw(self.display_surface)
        
        self.player.update(self.items)
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        for item in self.items:
            if not item.collected:
                pygame.draw.rect(self.display_surface, "white", item.rect)
        
        
