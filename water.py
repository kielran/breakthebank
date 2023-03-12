import pygame
from tiles import Tile

class Water():
    def __init__(self, tiles, startX, endX):
        self.tiles = tiles
        self.startX = startX
        self.endX = endX
    def draw(self, surface):
        self.tiles.draw(surface)
        
    def clean(self, tilesGroup):
        for water in self.tiles.sprites():
            tile = Tile((water.rect.topleft[0],water.rect.topleft[1]), "./imgs/floor1.png")
            tilesGroup.add(tile)
            water.kill()
        
    
        
    