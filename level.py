import pygame, sys
from tiles import Tile
from player import Janitor, Banker
from enemy import Roomba
from item import JanitorItem, BankerItem
from exit import JanitorExit, BankerExit
from obstacle import PointObstacle, InteractObstacle

class Level:
    def __init__(self, level_map, level_param, surface):
        self.display_surface = surface
        self.level_map = level_map
        self.level_param = level_param
        self.setup_level(level_map, level_param)

    def setup_level(self, layout, level_param):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        tile_size = 46
        currParam = 0
        for row_index, row in enumerate(layout):
            # print(row_index)
            # print(row)
            for col_index, cell in enumerate(row):
                cell = layout[row_index][col_index]
                #print(f'{row_index},{col_index}:{cell}')
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == "X":    
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

                if cell == "J":
                    player_sprite = Janitor((x,y-34))
                    self.player.add(player_sprite)
                    
                if cell == "B":
                    player_sprite = Banker((x,y-34))
                    self.player.add(player_sprite)
                    
                if cell == "E":
                    enemy_distance = level_param[currParam][0]
                    enemy_speed = level_param[currParam][1]
                    currParam += 1
                    roomba_sprite = Roomba((x, y), enemy_distance, enemy_speed, self.player)
                    self.enemies.add(roomba_sprite)
                
                if cell == "F":
                    janitor_item_sprite = JanitorItem((x, y), (64, 32))
                    self.items.add(janitor_item_sprite)
                
                if cell == "G":
                    banker_item_sprite = BankerItem((x, y), (64, 32))
                    self.items.add(banker_item_sprite)
                    
                if cell == "C":
                    point = PointObstacle((x,y), tile_size)
                    self.points.add(point)
                
                if cell == "O":
                    obstacle = InteractObstacle((x,y), tile_size)
                    self.obstacles.add(obstacle)
                    
                if cell == "N":
                    janitor_exit = JanitorExit((x,y))
                    self.exits.add(janitor_exit)
                    
                if cell == "M":
                    banker_exit = BankerExit((x,y))
                    self.exits.add(banker_exit)

    def horizontal_movement_collision(self):
        player = self.player.sprite  
        player.rect.x += player.direction.x * player.speed
        # for enemy in self.enemies.sprites():
        #     enemy.rect.x += enemy.direction * enemy.speed

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(player.rect): #if player collides with a tile
                if player.direction.x < 0: #moving left
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: #moving right
                    player.rect.right = sprite.rect.left
                    
            # for enemy in self.enemies.sprites():
            #     if sprite.rect.colliderect(enemy.rect): #if enemy collides with a tile
            #         if enemy.direction < 0: #moving left
            #             enemy.rect.left = sprite.rect.right
            #         elif enemy.direction > 0: #moving right
            #             enemy.rect.right = sprite.rect.left
                    
      
        for sprite in self.obstacles.sprites(): # Same as above but with obstacles
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
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
                if sprite.rect.colliderect(item.rect): #if item collides with a tile
                
                    if item.direction.y > 0: #moving left
                        item.rect.bottom = sprite.rect.top
                        item.direction.y = 0

                    elif item.direction.y < 0: #moving right
                        item.rect.top = sprite.rect.bottom
                        item.direction.y = 0
            
                        
        for sprite in self.obstacles.sprites(): # Same as above but with obstacles
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
    # For later: store in items/score increase
    def disappear_on_touch_obstacle(self):
        player = self.player.sprite
        for sprite in self.points.sprites(): # looking through all point locations
            if sprite.rect.colliderect(player.rect): # if player collides, remove
                print('Point collection')
                sprite.kill()
    
    # For later: generalize key for player/objects that can make them disappear
    def obstacle_behavior(self):
        player = self.player.sprite
        for sprite in self.obstacles.sprites(): # looking through all obstacles
            if sprite.rect.left == player.rect.right or sprite.rect.right == player.rect.left: # if the player is next to the obstacle
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN: # if key is pressed
                        if event.key == pygame.K_k and len(player.inventory) > 0: # and it is the interact button, remove
                            print('Obstacle collision')
                            sprite.kill()
                            
    def check_game_ended(self):
        player = self.player.sprite
        for exit in self.exits.sprites():
            if player.rect.colliderect(exit):
                if not ((type(self.player) == Banker and type(exit) == BankerExit) or (type(self.player) == Janitor and type(exit) == JanitorExit)):
                    return False
            else:
                return False
        
        return True
                    
                    

    def run(self):
        self.tiles.draw(self.display_surface)
        
        self.obstacles.draw(self.display_surface)

        self.points.draw(self.display_surface)
        
        self.exits.draw(self.display_surface)
        
        for enemy in self.enemies:
            sight_rect = enemy.update()
            #pygame.draw.rect(self.display_surface, "white", sight_rect)   #comment out to not draw the sight rect
            for player in self.player:
                if enemy.detect_player(player.rect, self.tiles):
                    print("detected")
                    return False
        self.enemies.draw(self.display_surface)
        
        self.player.update(self.items)
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.disappear_on_touch_obstacle()
        self.obstacle_behavior()
        
        for item in self.items:
            self.display_surface.blit(item.image, item.rect)
        
        if self.check_game_ended():
             return False                      
        return True
            
