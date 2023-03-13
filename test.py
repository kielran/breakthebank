import pygame
from level import Level
from settings import *
import unittest
# import pynput
# from pynput.keyboard import Key, Controller
import time


# keyboard = Controller()

# def press(key, start, end, counter):
#     if counter >= start and counter <= end:
#         keyboard.press(key)

# def releaseAll():
#     keyboard.release('w')
#     keyboard.release('d')
#     keyboard.release('s')
#     keyboard.release('a')
#     keyboard.release('k')
#     keyboard.release('j')
        
def testArrange1():
    pygame.init()
    screen = pygame.display.set_mode([80*16, 80*9])
    return Level(level_map_test, leveltest_param, screen, "./imgs/stage1_lobby.png"), screen


def testArrangeGravity():
    pygame.init()
    screen = pygame.display.set_mode([80*16, 80*9])
    return Level(level_map_test_gravity, leveltest_param, screen, "./imgs/stage1_lobby.png"), screen


class Testjanitor(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        originalX = self.level.janitor.sprite.rect.x
        originalY = self.level.janitor.sprite.rect.y
        c = 0
        while c < 20:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()
        
        self.assertEqual(self.level.janitor.sprite.rect.x, originalX)
        self.assertEqual(self.level.janitor.sprite.rect.y, originalY)

class Testbanker(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        originalX = self.level.banker.sprite.rect.x
        originalY = self.level.banker.sprite.rect.y
        c = 0
        while c < 20:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()
        
        self.assertEqual(self.level.banker.sprite.rect.x, originalX)
        self.assertEqual(self.level.banker.sprite.rect.y, originalY)

class Testexits(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        # for x in self.level.exits.sprites():
        #     topleft = x.rect.topleft
        #             c = 0
        # while c < 20:
        #     self.level.run()
        #     timer = pygame.time.Clock()
        #     # print(originaltopleft0)
        #     timer.tick(60)
        #     c += 1
        #     pygame.display.update()
        #     self.assertEqual(x.rect.topleft, topleft)
        originaltopleft0 = self.level.exits.sprites()[0].rect.topleft
        originaltopleft1 = self.level.exits.sprites()[1].rect.topleft
        c = 0
        while c < 20:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()
        self.assertEqual(self.level.exits.sprites()[1].rect.topleft, originaltopleft1)
        self.assertEqual(self.level.exits.sprites()[0].rect.topleft, originaltopleft0)
       
        # self.assertEqual(self.level.exits.rect[1].y, originalY)
    
class Testobstacles(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        for x in self.level.obstacles.sprites():
            topleft = x.rect.topleft
            c = 0
            while c < 20:
                self.level.run()
                timer = pygame.time.Clock()
                # print(originaltopleft0)
                timer.tick(60)
                c += 1
                pygame.display.update()
            self.assertEqual(x.rect.topleft, topleft)
       

    
class Testlevers(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        for x in self.level.levers.sprites():
            topleft = x.rect.topleft
            c = 0
            while c < 20:
                self.level.run()
                timer = pygame.time.Clock()
                # print(originaltopleft0)
                timer.tick(60)
                c += 1
                pygame.display.update()

            self.assertEqual(x.rect.topleft, topleft)
       
class Testenemy(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        originaltopleft0 = self.level.enemies.sprites()[0].rect.topleft
        c = 0
        while c < 20:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()

        self.assertNotEqual(self.level.enemies.sprites()[0].rect.topleft, originaltopleft0)
    
    

class Testitems_janitor(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        # print(self.level.items.sprites()[0])
        originaltopleft0 = self.level.items.sprites()[0].rect.topleft
        c = 0
        while c < 60:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()

        self.assertEqual(self.level.items.sprites()[0].rect.topleft, originaltopleft0)

class Testitems_banker(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrange1()
        # print(self.level.items.sprites()[0])
        originaltopleft0 = self.level.items.sprites()[1].rect.topleft
        c = 0
        while c < 60:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()

        self.assertEqual(self.level.items.sprites()[1].rect.topleft, originaltopleft0)
    
    


class Test_janitor_gravity(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrangeGravity()
        originalX = self.level.janitor.sprite.rect.x
        originalY = self.level.janitor.sprite.rect.y
        c = 0
        while c < 20:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()
        
        self.assertEqual(self.level.janitor.sprite.rect.x, originalX)
        self.assertNotEqual(self.level.janitor.sprite.rect.y, originalY)

class Test_banker_gravity(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrangeGravity()
        originalX = self.level.banker.sprite.rect.x
        originalY = self.level.banker.sprite.rect.y
        c = 0
        while c < 20:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()
        
        self.assertEqual(self.level.banker.sprite.rect.x, originalX)
        self.assertNotEqual(self.level.banker.sprite.rect.y, originalY)


class Test_items_janitor_gravity(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrangeGravity()
        # print(self.level.items.sprites()[0])
        originaltopleft0 = self.level.items.sprites()[0].rect.topleft
        c = 0
        while c < 60:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()

        self.assertNotEqual(self.level.items.sprites()[0].rect.topleft, originaltopleft0)

class Test_items_banker_gravity(unittest.TestCase):  
        
    def test_CheckSpawn(self): 
        self.level, self.screen = testArrangeGravity()
        # print(self.level.items.sprites()[0])
        originaltopleft0 = self.level.items.sprites()[1].rect.topleft
        c = 0
        while c < 60:
            self.level.run()
            timer = pygame.time.Clock()
            # print(originaltopleft0)
            timer.tick(60)
            c += 1
            pygame.display.update()

        self.assertNotEqual(self.level.items.sprites()[1].rect.topleft, originaltopleft0)
    


    # def test_CheckjanitorDetected(self): 
    #     self.level, self.screen = testArrange()
        
    #     c = 0
    #     timer = pygame.time.Clock()
    #     janitorDetected = False
    #     while c < 250:
    #         self.screen.fill('black')
            
    #         #Movement
    #         press('w', 21, 21, c)
    #         press('d', 20, 60, c)
    #         #press('w', 65, 65, c)
    #         press('d', 66, 100, c)   
    #         #press('a', 121, 135, c)     
            
    #         pygame.event.get()
    #         if not self.level.run():
    #             print("janitor died")
    #             janitorDetected = True
    #             break
            
    #         releaseAll()
            
    #         timer.tick(60)
    #         c += 1
    #         pygame.display.update()
            
    #     self.assertTrue(janitorDetected)
        
        
        

if __name__ == '__main__':
    unittest.main()


