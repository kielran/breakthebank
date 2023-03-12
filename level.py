import pygame, sys
from tiles import Tile
from player import Janitor, Banker
from enemy import Roomba
from item import JanitorItem, BankerItem
from exit import JanitorExit, BankerExit
from obstacle import PointObstacle, InteractObstacle, InteractBox

class Level:
    def __init__(self, level_map, level_param, surface, bg_image):
        self.display_surface = surface
        self.level_map = level_map
        self.level_param = level_param
        self.bg_image = pygame.image.load(bg_image).convert_alpha()
        self.setup_level(level_map, level_param)

    def setup_level(self, layout, level_param):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.banker = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.levers = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        tile_size = 46
        currParam = 0
        for row_index, row in enumerate(layout):
            # print(row_index)
            # print(row)
            cols_skipped = 0
            for col_index, cell in enumerate(row):
                cell = layout[row_index][col_index]
                #print(f'{row_index},{col_index}:{cell}')
                x = (col_index - cols_skipped) * tile_size
                y = row_index * tile_size
                
                if cell == "X":    
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

                if cell == "J":
                    player_sprite = Janitor((x,y))
                    self.player.add(player_sprite)
                    
                if cell == "B":
                    player_sprite = Banker((x,y))
                    self.player.add(player_sprite)
                
                if cell == "B":
                    banker_sprite = Banker((x,y))
                    self.banker.add(banker_sprite)
                    
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
                    
                if cell == "N":
                    janitor_exit = JanitorExit((x,y))
                    self.exits.add(janitor_exit)
                    
                if cell == "M":
                    banker_exit = BankerExit((x,y))
                    self.exits.add(banker_exit)

    def horizontal_movement_collision(self):
        player = self.player.sprite  
        player.rect.x += player.direction.x * player.speed
        banker = self.banker.sprite  
        banker.rect.x += banker.direction.x * banker.speed
        # for enemy in self.enemies.sprites():
        #     enemy.rect.x += enemy.direction * enemy.speed

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
                    print('NAN')
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
        
        banker_is_colliding_with_tile = False
        janitor_is_colliding_with_tile = False

        for item in self.items:
            item.apply_gravity()
        
        for sprite in self.tiles.sprites(): #Looking through all tiles on map
            if sprite.rect.colliderect(player.rect): #If player 1 collides with a tile
                janitor_is_colliding_with_tile = True
                if player.direction.y > 0: #Moving up
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_on_ground = True
                elif player.direction.y < 0: #Moving down
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.is_on_ground = False
            if sprite.rect.colliderect(banker.rect): #If player 2 collides with a tile
                banker_is_colliding_with_tile = True
                if banker.direction.y > 0: #Moving up
                    banker.rect.bottom = sprite.rect.top
                    banker.direction.y = 0
                    banker.is_on_ground = True
                elif banker.direction.y < 0: #Moving down
                    banker.rect.top = sprite.rect.bottom
                    banker.direction.y = 0
                    banker.is_on_ground = False


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
        if janitor_is_colliding_with_tile == False:
            player.is_on_ground = False

        if banker_is_colliding_with_tile == False:
            banker.is_on_ground = False


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
                                else:
                                    print('Player 1 does not have an item, cannot remove')
                if sprite.rect.left == banker.rect.right or sprite.rect.right == banker.rect.left: #If player 2 is next to the obstacle
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_SLASH: #and it is player 2's interact button (/), remove
                                if(len(banker.inventory) > 0):
                                    print('Player 2 (Arrows) with key encountered door, removing')
                                    sprite.kill()
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
        self.display_surface.blit(self.bg_image, (0,0))
        self.tiles.draw(self.display_surface)
        
        self.obstacles.draw(self.display_surface)

        self.points.draw(self.display_surface)

        self.levers.draw(self.display_surface)
        
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
        
        self.banker.update(self.items)
        self.banker.draw(self.display_surface)
        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        self.obstacle_behavior()
        self.lever_flip()
        
        for item in self.items:
            self.display_surface.blit(item.image, item.rect)
        
        if self.check_game_ended():
             return False                      
        return True
