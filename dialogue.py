import pygame, sys

# dialogue should contain info on every snapshot moment
# someone says something, so all the text elements
# and arrangements 

textColor = (255, 255, 255)
boxColor = (0, 0, 0)

class Dialogue:
    def __init__(self, screen, speaker, listener, midtext):
        self.screen = screen
        self.text = midtext
        self.speaker = speaker
        self.listener = listener        
        self.p1 = pygame.image.load(speaker).convert()
        self.p2 = pygame.image.load(listener).convert()

    def loadFrame(self):
        #place the black text box over it
        # self.surface = pygame.display.set_mode((1280, 720))
        # pygame.draw.rect(self.screen, boxColor, (50, 50, 60, 60))
        # pygame.display.flip()
        #place the speaker and listener images
        self.screen.blit(self.p1, (300, 0))
        pygame.display.update()

        #pygame.display.set_caption(midtext)
        font_obj = pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf", 25)
        text_obj = font_obj.render(self.text, True, (255, 255, 255), None)

        self.screen.blit(text_obj, (22,0))

       

        #place the text in the text box

        #pass
