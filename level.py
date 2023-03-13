import pygame, sys
from tiles import Tile
from player import Janitor, Banker
from enemy import Roomba
from item import JanitorItem, BankerItem
from exit import JanitorExit, BankerExit
from obstacle import PointObstacle, InteractObstacle, InteractBox
from water import Water
from elevator import Elevator

class Level:
    def __init__(self, level_map, level_param, surface, bg_image):
        self.display_surface = surface
        self.level_map = level_map
        self.level_param = level_param
        self.bg_image = pygame.image.load(bg_image).convert_alpha()
        self.setup_level(level_map, level_param)
        self.score = 0

    def setup_level(self, layout, level_param):
        self.tiles = pygame.sprite.Group()
        self.janitor = pygame.sprite.GroupSingle()
        self.banker = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.levers = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.elevators = pygame.sprite.Group()
        self.water = []
        tile_size = 46
        currParam = 0
        col_index = 0
        row_index = 0
        while row_index < len(layout):
            # print(row_index)
            # print(row)
            row = layout[row_index]
            col_index = 0
            while col_index < len(row):
                cell = layout[row_index][col_index]
                #print(f'{row_index},{col_index}:{cell}')
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == "X":    
                    tile = Tile((x,y), "./imgs/floor1.png")
                    self.tiles.add(tile)

                if cell == "J":
                    player_sprite = Janitor((x,y+8))
                    self.janitor.add(player_sprite)
                              
                if cell == "B":
                    banker_sprite = Banker((x,y+8))
                    self.banker.add(banker_sprite)
                    
                if cell == "E":
                    enemy_distance = level_param[currParam][0]
                    enemy_speed = level_param[currParam][1]
                    currParam += 1
                    roomba_sprite = Roomba((x, y), enemy_distance, enemy_speed)
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
                    uniqueID = level_param[currParam][0]
                    currParam += 1
                    obstacle = InteractObstacle((x, y + tile_size), tile_size, tile_size * 3, uniqueID)
                    self.obstacles.add(obstacle)   
                           
                if cell == "L":
                    uniqueID = level_param[currParam][0]
                    currParam += 1
                    lever = InteractBox((x,y), uniqueID)
                    self.levers.add(lever)
                    
                if cell == "N":
                    janitor_exit = JanitorExit((x,y))
                    self.exits.add(janitor_exit)
                    
                if cell == "M":
                    banker_exit = BankerExit((x,y))
                    self.exits.add(banker_exit)
                    
                if cell == "Z":
                    elevator_distance = level_param[currParam][0]
                    elevator_speed = level_param[currParam][1] 
                    elevator = Elevator((x, y), elevator_distance, elevator_speed)
                    self.elevators.add(elevator)
                    
                if cell == "W":
                    water_tiles = pygame.sprite.Group()
                    startX = x
                    while col_index < len(row) and layout[row_index][col_index] == "W":
                        x = col_index * tile_size
                        y = row_index * tile_size
                        water = Tile((x,y), "./imgs/water.png")
                        water_tiles.add(water)
                        col_index += 1
                    col_index -= 1
                    endX = x + 46
                    water_object = Water(water_tiles, startX, endX, y)
                    self.water.append(water_object)
                    print(self.water)
                    
                col_index += 1
            row_index += 1
                    
                    
                    
                

    def horizontal_movement_collision(self):
        janitor = self.janitor.sprite  
        janitor.rect.x += janitor.direction.x * janitor.speed
        banker = self.banker.sprite  
        banker.rect.x += banker.direction.x * banker.speed
        # for enemy in self.enemies.sprites():
        #     enemy.rect.x += enemy.direction * enemy.speed

        for sprite in self.tiles.sprites(): #Looking through all tiles on map (x axis)
            if sprite.rect.colliderect(janitor.rect): #If janitor 1 collides with a tile
                if janitor.direction.x < 0: #Moving right
                    janitor.rect.left = sprite.rect.right
                elif janitor.direction.x > 0: #Moving left
                    janitor.rect.right = sprite.rect.left
            if sprite.rect.colliderect(banker.rect): #If janitor 2 collides with a tile
                if banker.direction.x < 0: #Moving right
                    banker.rect.left = sprite.rect.right
                elif banker.direction.x > 0: #Moving left
                    banker.rect.right = sprite.rect.left
                    
        for sprite in self.elevators.sprites(): #Looking through all tiles on map (x axis)
            if sprite.rect.colliderect(janitor.rect): #If janitor 1 collides with a tile
                if janitor.direction.x < 0: #Moving right
                    janitor.rect.left = sprite.rect.right
                elif janitor.direction.x > 0: #Moving left
                    janitor.rect.right = sprite.rect.left
            if sprite.rect.colliderect(banker.rect): #If janitor 2 collides with a tile
                if banker.direction.x < 0: #Moving right
                    banker.rect.left = sprite.rect.right
                elif banker.direction.x > 0: #Moving left
                    banker.rect.right = sprite.rect.left
                    
            # for enemy in self.enemies.sprites():
            #     if sprite.rect.colliderect(enemy.rect): #if enemy collides with a tile
            #         if enemy.direction < 0: #moving left
            #             enemy.rect.left = sprite.rect.right
            #         elif enemy.direction > 0: #moving right
            #             enemy.rect.right = sprite.rect.left
                    
        for sprite in self.obstacles.sprites(): # Same as above but with obstacles
            if sprite.rect.colliderect(janitor.rect):
                if janitor.direction.x < 0:
                    janitor.rect.left = sprite.rect.right
                elif janitor.direction.x > 0: #Moving left
                    janitor.rect.right = sprite.rect.left
            if sprite.rect.colliderect(banker.rect): #If janitor 2 collides with an obstacle
                if banker.direction.x < 0: #Moving right
                    banker.rect.left = sprite.rect.right 
                elif banker.direction.x > 0: #Moving left
                    banker.rect.right = sprite.rect.left
            
        for sprite in self.levers.sprites(): # Looking through all levers on map (x axis)
            if sprite.rect.colliderect(janitor.rect): #If janitor 1 collides with a lever
                if janitor.direction.x < 0: #Moving right
                    janitor.rect.left = sprite.rect.right
                elif janitor.direction.x > 0: #Moving left
                    janitor.rect.right = sprite.rect.left
            if sprite.rect.colliderect(banker.rect): #If janitor 2 collides with a lever
                if banker.direction.x < 0: #Moving right
                    banker.rect.left = sprite.rect.right 
                elif banker.direction.x > 0: #Moving left
                    banker.rect.right = sprite.rect.left
                

    def vertical_movement_collision(self):
        janitor = self.janitor.sprite
        janitor.apply_gravity()
        banker = self.banker.sprite
        banker.apply_gravity()
        
        banker_is_colliding_with_tile = False
        janitor_is_colliding_with_tile = False

        for item in self.items:
            item.apply_gravity()
        
        for sprite in self.tiles.sprites(): #Looking through all tiles on map
            if sprite.rect.colliderect(janitor.rect): #If janitor collides with a tile
                janitor_is_colliding_with_tile = True
                if janitor.direction.y > 0: #Moving up
                    janitor.rect.bottom = sprite.rect.top
                    janitor.direction.y = 0
                    janitor.is_on_ground = True
                elif janitor.direction.y < 0: #Moving down
                    janitor.rect.top = sprite.rect.bottom
                    janitor.direction.y = 0
                    janitor.is_on_ground = False
            if sprite.rect.colliderect(banker.rect): #If banker collides with a tile
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
                        
        for waterObject in self.water:
            for waterTile in waterObject.tiles:
                if waterTile.rect.colliderect(janitor.rect): #If janitor collides with a tile
                    janitor_is_colliding_with_tile = True
                    if janitor.direction.y > 0: #Moving up
                        janitor.rect.bottom = sprite.rect.top
                        janitor.direction.y = 0
                        janitor.is_on_ground = True
                    elif janitor.direction.y < 0: #Moving down
                        janitor.rect.top = sprite.rect.bottom
                        janitor.direction.y = 0
                        janitor.is_on_ground = False
                # if waterTile.rect.colliderect(banker.rect): #If banker collides with a tile
                #     banker_is_colliding_with_tile = True
                #     if banker.direction.y > 0: #Moving up
                #         banker.rect.bottom = sprite.rect.top
                #         banker.direction.y = 0
                #         banker.is_on_ground = True
                #     elif banker.direction.y < 0: #Moving down
                #         banker.rect.top = sprite.rect.bottom
                #         banker.direction.y = 0
                #         banker.is_on_ground = False
                        
        for sprite in self.elevators.sprites(): #Looking through all tiles on map
            if sprite.rect.colliderect(janitor.rect): #If janitor collides with a tile
                janitor_is_colliding_with_tile = True
                if janitor.direction.y > 0: #Moving up
                    janitor.rect.bottom = sprite.rect.top
                    janitor.direction.y = 0
                    janitor.is_on_ground = True
                elif janitor.direction.y < 0: #Moving down
                    janitor.rect.top = sprite.rect.bottom
                    janitor.direction.y = 0
                    janitor.is_on_ground = False
            if sprite.rect.colliderect(banker.rect): #If banker collides with a tile
                banker_is_colliding_with_tile = True
                if banker.direction.y > 0: #Moving up
                    banker.rect.bottom = sprite.rect.top
                    banker.direction.y = 0
                    banker.is_on_ground = True
                elif banker.direction.y < 0: #Moving down
                    banker.rect.top = sprite.rect.bottom
                    banker.direction.y = 0
                    banker.is_on_ground = False
            
                        
        for sprite in self.obstacles.sprites(): #Looking through all obstacles (y axis)
            if sprite.rect.colliderect(janitor.rect): #If janitor 1 collides with an obstacle
                if janitor.direction.y > 0: #Moving up
                    janitor.rect.bottom = sprite.rect.top
                    janitor.direction.y = 0
                elif janitor.direction.y < 0: #Moving down
                    janitor.rect.top = sprite.rect.bottom
                    janitor.direction.y = 0
            if sprite.rect.colliderect(banker.rect): #If janitor 2 collides with an obstacle
                if banker.direction.y > 0: #Moving up
                    banker.rect.bottom = sprite.rect.top
                    banker.direction.y = 0
                elif banker.direction.y < 0: #Moving down
                    banker.rect.top = sprite.rect.bottom
                    banker.direction.y = 0
        if janitor_is_colliding_with_tile == False:
            janitor.is_on_ground = False

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
        janitor = self.janitor.sprite
        banker = self.banker.sprite

        for sprite in self.points.sprites(): #Looking through all point locations
            if sprite.rect.colliderect(janitor.rect) or sprite.rect.colliderect(banker.rect): #If either player collides, remove
                print('Point collection')
                sprite.kill()
                self.score += 100

        for sprite in self.obstacles.sprites(): #Looking through all obstacles
            if sprite.obstacleID == 0: #If the obstacle is the generic obstacle door
                if sprite.rect.left == janitor.rect.right or sprite.rect.right == janitor.rect.left: #If player 1 is next to the obstacle
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_s: #and it is player 1's interact button (F), remove
                                if(len(janitor.inventory) > 0):
                                    print('Player 1 (WASD) with key encountered door, removing')
                                    sprite.kill()
                                else:
                                    print('Player 1 does not have an item, cannot remove')
                if sprite.rect.left == banker.rect.right or sprite.rect.right == banker.rect.left: #If player 2 is next to the obstacle
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_DOWN: #and it is player 2's interact button (/), remove
                                if(len(banker.inventory) > 0):
                                    print('Player 2 (Arrows) with key encountered door, removing')
                                    sprite.kill()
                                else:
                                    print('Player 2 does not have an item, cannot remove')

    def lever_flip(self):
        janitor = self.janitor.sprite
        banker = self.banker.sprite

        for sprite in self.levers.sprites(): #Looking through all levers
            if sprite.flipUse == 1: #If the lever hasn't been flipped (Player 1 always has priority over Player 2)
                if sprite.rect.left == janitor.rect.right or sprite.rect.right == janitor.rect.left: #If player 1 is next to the lever
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: #If a key is pressed
                            if event.key == pygame.K_s: #and it is player 1's interact button (F)
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
                            if event.key == pygame.K_DOWN: #and it is player 2's interact button (/)
                                for spriteOb in self.obstacles.sprites():
                                    if spriteOb.obstacleID == sprite.leverID: #delete the corresponding object to lever ID
                                        print('Player 2 flipped lever, obstacle of id ' + str(spriteOb.obstacleID) + ' is removed')
                                        spriteOb.kill()
                                        break
                                sprite.flipUse = 0 #Lever can no longer be used
                                sprite.update() #Update lever sprite to being flipped
      
    def check_banker_on_water(self):
        bankerRect = self.banker.sprite.rect
        
        for waterObject in self.water:
            if waterObject.active:
                for waterTile in waterObject.tiles:
                    if bankerRect.colliderect(waterTile.rect) or (bankerRect.midbottom[1] == waterObject.Y and bankerRect.bottomleft[0] < waterObject.endX - 10 and bankerRect.bottomright[0] > waterObject.startX + 10):
                        return True

    def check_game_ended(self):
        janitor = self.janitor.sprite
        banker = self.banker.sprite
        for exit in self.exits.sprites():
            if janitor.rect.colliderect(exit):
                if not type(exit) == JanitorExit:
                    return False
            elif banker.rect.colliderect(exit):
                if not type(exit) == BankerExit:
                    return False
            else:
                return False
        
        return True
                    

    def run(self):
        self.display_surface.blit(self.bg_image, (0,0))
        self.tiles.draw(self.display_surface)
        
        for water in self.water:
            water.draw(self.display_surface)
        
        self.obstacles.draw(self.display_surface)

        self.points.draw(self.display_surface)

        self.levers.draw(self.display_surface)
        
        self.exits.draw(self.display_surface)
        
        self.elevators.update(self.banker.sprite, self.janitor.sprite)
        self.elevators.draw(self.display_surface)
        
        for enemy in self.enemies:
            sight_rect = enemy.update()
            #pygame.draw.rect(self.display_surface, "white", sight_rect)   #comment out to not draw the sight rect
            if enemy.detect_player(self.janitor.sprite.rect, self.tiles):
                print(enemy.distance)
                return False, "loss"
            if enemy.detect_player(self.banker.sprite.rect, self.tiles):
                print("detected")
                return False, "loss"
        self.enemies.draw(self.display_surface)
        
        self.janitor.update(self.items, self.water, self.tiles)
        self.janitor.draw(self.display_surface)
        
        self.banker.update(self.items, self.elevators, self.janitor.sprite)
        self.banker.draw(self.display_surface)
        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        self.obstacle_behavior()
        self.lever_flip()

        textFont = pygame.font.SysFont('timesnewroman', 40)
        scoreText = textFont.render(f'{self.score}', False, 'Black')
        scoreRect = scoreText.get_rect(topleft = (6, 6))
        self.display_surface.blit(scoreText, scoreRect)
        
        for item in self.items:
            self.display_surface.blit(item.image, item.rect)
        
        if self.check_banker_on_water():
            return False, "loss"
        if self.check_game_ended():
             return False, "win"                      
        return True, ""