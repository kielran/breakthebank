import pygame
from level import Level
from settings import *
import unittest
import pynput
from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

def press(key, start, end, counter):
    if counter >= start and counter <= end:
        keyboard.press(key)

def releaseAll():
    keyboard.release('w')
    keyboard.release('d')
    keyboard.release('s')
    keyboard.release('a')
    keyboard.release('k')
    keyboard.release('j')
        
def testArrange():
    pygame.init()
    screen = pygame.display.set_mode([80*16, 80*9])
    screen.fill('black')
    return Level(level_map, level_param, screen), screen

class TestPlayer(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange()
        originalX = self.level.player.sprite.rect.x
        originalY = self.level.player.sprite.rect.y
        time.sleep(1)
        
        self.assertEqual(self.level.player.sprite.rect.x, originalX)
        self.assertEqual(self.level.player.sprite.rect.y, originalY)
    
    def test_CheckPlayerDetected(self): 
        self.level, self.screen = testArrange()
        
        c = 0
        timer = pygame.time.Clock()
        playerDetected = False
        while c < 250:
            self.screen.fill('black')
            
            #Movement
            press('w', 21, 21, c)
            press('d', 20, 60, c)
            #press('w', 65, 65, c)
            press('d', 66, 100, c)   
            #press('a', 121, 135, c)     
            
            pygame.event.get()
            if not self.level.run():
                print("player died")
                playerDetected = True
                break
            
            releaseAll()
            
            timer.tick(60)
            c += 1
            pygame.display.update()
            
        self.assertTrue(playerDetected)
        
        
        

if __name__ == '__main__':
    unittest.main()


