import pygame
from tiles import Tile
from player import Player
from banker import Banker
from obstacle import PointObstacle
from obstacle import InteractObstacle
from obstacle import InteractBox
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
        self.banker = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.levers = pygame.sprite.Group()
        tile_size = 46
        for row_index, row in enumerate(layout):
            # print(row_index)
            # print(row)

            cols_skipped = 0
            for col_index, cell in enumerate(row):
                #print(f'{row_index},{col_index}:{cell}')
                x = (col_index - cols_skipped) * tile_size
                y = row_index * tile_size
                
                if cell == "X":    
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                
                if cell == "B":
                    banker_sprite = Banker((x,y))
                    self.banker.add(banker_sprite)
                    
                if cell == "E":
                    roomba_sprite = Roomba((x, y), 300, self.player)
                    self.enemies.add(roomba_sprite)
                
                if cell == "J":
                    janitor_item_sprite = JanitorItem((x, y), (tile_size, tile_size), "./imgs/key.png")
                    self.items.add(janitor_item_sprite)
                
                if cell == "K":
                    banker_item_sprite = BankerItem((x, y), (tile_size, tile_size), "./imgs/key.png")
                    self.items.add(banker_item_sprite)
                    
                if cell == "C":
                    point = PointObstacle((x,y), tile_size)
                    self.points.add(point)
                
                if cell == "O":
                    obstacle = InteractObstacle((x, y + tile_size), tile_size, tile_size * 3)
                    if col_index + 1 < len(row) and layout[row_index][col_index + 1].isnumeric():
                        col_index += 1
                        cols_skipped += 1
                        uniqueID = layout[row_index][col_index]
                        obstacle.obstacleID = int(uniqueID)
                    self.obstacles.add(obstacle)   
                           
                if cell == "L":
                    lever = InteractBox((x,y))
                    if col_index + 1 < len(row) and layout[row_index][col_index + 1].isnumeric():
                        col_index += 1
                        cols_skipped += 1
                        uniqueID = layout[row_index][col_index]
                        lever.leverID = int(uniqueID)
                    self.levers.add(lever)

    def horizontal_movement_collision(self):
        player = self.player.sprite  
        player.rect.x += player.direction.x * player.speed
        banker = self.banker.sprite  
        banker.rect.x += banker.direction.x * banker.speed

        for sprite in self.tiles.sprites(): #Looking through all tiles on map (x axis)
            if sprite.rect.colliderect(player.rect): #If player 1 collides with a tile
                if player.direction.x < 0: #Moving right
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: #Moving left
                    player.rect.right = sprite.rect.left
            if sprite.rect.colliderect(banker.rect): #If player 2 collides with a tile
                if banker.direction.x < 0: #Moving right
                    banker.rect.left = sprite.rect.right
                elif banker.direction.x > 0: #Moving left
                    banker.rect.right = sprite.rect.left
                    
        for sprite in self.obstacles.sprites(): #Looking through all obstacles on map (x axis)
            if sprite.rect.colliderect(player.rect): #If player 1 collides with an obstacle
                if player.direction.x < 0: #Moving right
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: #Moving left
                    player.rect.right = sprite.rect.left
            if sprite.rect.colliderect(banker.rect): #If player 2 collides with an obstacle
                if banker.direction.x < 0: #Moving right
                    banker.rect.left = sprite.rect.right 
                elif banker.direction.x > 0: #Moving left
                    banker.rect.right = sprite.rect.left
            
        for sprite in self.levers.sprites(): # Looking through all levers on map (x axis)
            if sprite.rect.colliderect(player.rect): #If player 1 collides with a lever
                if player.direction.x < 0: #Moving right
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: #Moving left
                    player.rect.right = sprite.rect.left
            if sprite.rect.colliderect(banker.rect): #If player 2 collides with a lever
                if banker.direction.x < 0: #Moving right
                    banker.rect.left = sprite.rect.right 
                elif banker.direction.x > 0: #Moving left
                    banker.rect.right = sprite.rect.left
                

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        banker = self.banker.sprite
        banker.apply_gravity()
        
        for item in self.items:
            item.apply_gravity()
        
        for sprite in self.tiles.sprites(): #Looking through all tiles on map
            if sprite.rect.colliderect(player.rect): #If player 1 collides with a tile
                if player.direction.y > 0: #Moving up
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0: #Moving down
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
            if sprite.rect.colliderect(banker.rect): #If player 2 collides with a tile
                if banker.direction.y > 0: #Moving up
                    banker.rect.bottom = sprite.rect.top
                    banker.direction.y = 0
                elif banker.direction.y < 0: #Moving down
                    banker.rect.top = sprite.rect.bottom
                    banker.direction.y = 0
                    
            for item in self.items.sprites(): #Looking through all items (y axis)
                if sprite.rect.colliderect(item.rect): #If item collides with a tile
                    if item.direction.y > 0: #Moving up
                        item.rect.bottom = sprite.rect.top
                        item.direction.y = 0
                    elif item.direction.y < 0: #Moving down
                        item.rect.top = sprite.rect.bottom
                        item.direction.y = 0
                        
        for sprite in self.obstacles.sprites(): #Looking through all obstacles (y axis)
            if sprite.rect.colliderect(player.rect): #If player 1 collides with an obstacle
                if player.direction.y > 0: #Moving up
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0: #Moving down
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
            if sprite.rect.colliderect(banker.rect): #If player 2 collides with an obstacle
                if banker.direction.y > 0: #Moving up
                    banker.rect.bottom = sprite.rect.top
                    banker.direction.y = 0
                elif banker.direction.y < 0: #Moving down
                    banker.rect.top = sprite.rect.bottom
                    banker.direction.y = 0


    """
    def banker_horizontal_movement_collision(self):
        banker = self.banker.sprite  
        banker.rect.x += banker.direction.x * banker.speed

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(banker.rect): # If player 2 collides with a tile
                if banker.direction.x < 0: #moving left
                    banker.rect.left = sprite.rect.right
                elif banker.direction.x > 0: #moving right
                    banker.rect.right = sprite.rect.left

        for sprite in self.obstacles.sprites(): # Players can't overlap obstacles (x axis)
            if sprite.rect.colliderect(banker.rect):
                if banker.direction.x < 0:
                    banker.rect.left = sprite.rect.right 
                elif banker.direction.x > 0:
                    banker.rect.right = sprite.rect.left

    def banker_vertical_movement_collision(self):
        banker = self.banker.sprite
        banker.apply_gravity()

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(banker.rect): #if player collides with a tile
                if banker.direction.y > 0: #moving left
                    banker.rect.bottom = sprite.rect.top
                    banker.direction.y = 0
                elif banker.direction.y < 0: #moving right
                    banker.rect.top = sprite.rect.bottom
                    banker.direction.y = 0
    """


    # For later: gefneralize key for player/objects that can make them disappear
    def obstacle_behavior(self):
        player = self.player.sprite
        banker = self.banker.sprite

        for sprite in self.points.sprites(): #Looking through all point locations
            if sprite.rect.colliderect(player.rect) or sprite.rect.colliderect(banker.rect): #If either player collides, remove
                print('Point collection')
                sprite.kill()

        for sprite in self.obstacles.sprites(): #Looking through all obstacles
            if sprite.obstacleID == 0: #If the obstacle is the generic obstacle door
                if sprite.rect.left == player.rect.right or sprite.rect.right == player.rect.left: #If player 1 is next to the obstacle
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_f: #and it is player 1's interact button (F), remove
                                if(len(player.inventory) > 0):
                                    print('Player 1 (WASD) with key encountered door, removing')
                                    sprite.kill()
                                    player.inventory.clear()
                                else:
                                    print('Player 1 does not have an item, cannot remove')
                if sprite.rect.left == banker.rect.right or sprite.rect.right == banker.rect.left: #If player 2 is next to the obstacle
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_SLASH: #and it is player 2's interact button (/), remove
                                if(len(banker.inventory) > 0):
                                    print('Player 2 (WASD) with key encountered door, removing')
                                    sprite.kill()
                                    player.inventory.clear()
                                else:
                                    print('Player 2 does not have an item, cannot remove')

    def lever_flip(self):
        player = self.player.sprite
        banker = self.banker.sprite

        for sprite in self.levers.sprites(): #Looking through all levers
            if sprite.flipUse == 1: #If the lever hasn't been flipped (Player 1 always has priority over Player 2)
                if sprite.rect.left == player.rect.right or sprite.rect.right == player.rect.left: #If player 1 is next to the lever
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_f: #and it is player 1's interact button (F)
                                for spriteOb in self.obstacles.sprites():
                                    if spriteOb.obstacleID == sprite.leverID: #delete the corresponding object to lever ID
                                        print('Player 1 flipped lever, obstacle of id ' + str(spriteOb.obstacleID) + ' is removed')
                                        spriteOb.kill()
                                        break
                                sprite.flipUse = 0 #Lever can no longer be used
                                sprite.update() #Update lever sprite to being flipped
                if sprite.rect.left == banker.rect.right or sprite.rect.right == banker.rect.left: #If player 2 is next to the lever
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_SLASH: #and it is player 2's interact button (/)
                                for spriteOb in self.obstacles.sprites():
                                    if spriteOb.obstacleID == sprite.leverID: #delete the corresponding object to lever ID
                                        print('Player 2 flipped lever, obstacle of id ' + str(spriteOb.obstacleID) + ' is removed')
                                        spriteOb.kill()
                                        break
                                sprite.flipUse = 0 #Lever can no longer be used
                                sprite.update() #Update lever sprite to being flipped
            #else:
                #print('Lever id ' + str(sprite.leverID) + ' is deactivated')
                    

    def run(self):
        self.tiles.draw(self.display_surface)
        
        self.obstacles.draw(self.display_surface)

        self.points.draw(self.display_surface)

        self.levers.draw(self.display_surface)
        
        for enemy in self.enemies:
            sight_rect = enemy.update()
            #pygame.draw.rect(self.display_surface, "white", sight_rect)   #comment out to not draw the sight rect
            for player in self.player:
                if enemy.detect_player(player.rect, self.tiles):
                    print("detected")
        self.enemies.draw(self.display_surface)
        
        self.player.update(self.items)
        self.player.draw(self.display_surface)
        
        self.banker.update(self.items)
        self.banker.draw(self.display_surface)
        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        self.obstacle_behavior()
        self.lever_flip()
        
        for item in self.items:
            self.display_surface.blit(item.image, item.rect)
