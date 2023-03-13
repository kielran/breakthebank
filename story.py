import pygame, sys
from dialogue import Dialogue

# story should have data on
# images used (bg, janitor, banker sprites)
# a stageid so i can use the right one @ right time
# order to help with before/after the stage is cleared
# be careful because not sure how the win screen works
# order that dialogue is presented

class Story:
    def __init__(self, screen, bgimg):
        self.screen = screen
        self.background = bgimg
        self.dialogue = []
        self.bg = pygame.image.load(self.background)
    
    def readStory(self):
        self.screen.blit(self.bg, (0,0))
        pygame.display.update()
        
        pygame.event.clear()
        for x in self.dialogue: #start the loop first
            print("bruh)")
            x.loadFrame()
            wait()
                

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False

