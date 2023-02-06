# Simple pygame program

# Import and initialize the pygame library
import pygame
import os
pygame.init()

if not os.path.exists("imgs"):
    print("you do not have imgs folder")

# files:

pygame.display.set_caption('Break the Bank')


class button():
    def __init__(self, x,y,width,height, text='', color = None,image=None, hovering_image=None, amplifier=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = image
        self.hovering_image = hovering_image
        self.amplifier = amplifier

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if self.color != None:
            if outline:
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
        if self.image != None:
            if self.amplifier == None:
                if not self.isOver(pygame.mouse.get_pos()):
                    image = pygame.image.load(self.image)
                    rect_image = image.get_rect()
                    
                    image = pygame.transform.scale(image, ((rect_image.width/(237.5*16))*size*16,(rect_image.height/(237.5*9))*size*9))
                    
                else:
                    image = pygame.image.load(self.hovering_image)
                    rect_image = image.get_rect()
                    image = pygame.transform.scale(image, ((rect_image.width/(237.5*16))*size*16,(rect_image.height/(237.5*9))*size*9))
            else:
                if not self.isOver(pygame.mouse.get_pos()):
                    image = pygame.image.load(self.image)
                    rect_image = image.get_rect()
                    #print(rect_image)
                    image = pygame.transform.scale(image, ((rect_image.width/(self.amplifier*16))*size*16,(rect_image.height/(self.amplifier*9))*size*9))
                else:
                    image = pygame.image.load(self.hovering_image)
                    rect_image = image.get_rect()
                    image = pygame.transform.scale(image, ((rect_image.width/(self.amplifier*16))*size*16,(rect_image.height/(self.amplifier*9))*size*9))
            win.blit(image, (self.x, self.y))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if self.image == None:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
                
            return False
        elif self.amplifier == None:
            image = pygame.image.load(self.image)
            rect_image = image.get_rect()
            if pos[0] > self.x and pos[0] < self.x + (rect_image.width/(237.5*16))*size*16:
                if pos[1] > self.y and pos[1] < self.y + (rect_image.height/(237.5*9))*size*9:
                    return True
            
            return False
        else:
            image = pygame.image.load(self.image)
            rect_image = image.get_rect()
            if pos[0] > self.x and pos[0] < self.x + (rect_image.width/(self.amplifier*16))*size*16:
                if pos[1] > self.y and pos[1] < self.y + (rect_image.height/(self.amplifier*9))*size*9:
                    return True
            
            return False
size = 80

def drawMainMenu():
    backgroundphoto = pygame.image.load("imgs/start_bare.png").convert()
    #screen.blit(backgroundphoto, (0, 0))
    backgroundphoto = pygame.transform.scale(backgroundphoto, (size*16,size*9)) 
    screen.blit(backgroundphoto,(0,0))
    start_button.draw(screen)
    quit_button.draw(screen)
    audio_button.draw(screen)
    accessibility_button.draw(screen)

def drawPauseMenu():
    backgroundphoto = pygame.image.load("imgs/pause_bg.png").convert()
    backgroundphoto = pygame.transform.scale(backgroundphoto, (size*16,size*9))
    screen.blit(backgroundphoto,(0,0)) 
    continue_button.draw(screen)
    restart_button.draw(screen)
    tutorial_button.draw(screen)
    pause_title.draw(screen)
    quit_button.draw(screen)
    audio_button.draw(screen)
    accessibility_button.draw(screen)

    
#    green_button.draw(screen,(0,0,0))
    #quit_button.draw(screen,(0,0,0))


# Set up the drawing window
screen = pygame.display.set_mode([size*16, size*9])
# screen = pygame.transform.scale(backgroundphoto,[859, 727])
width = screen.get_width()
height = screen.get_height()


smallfont = pygame.font.SysFont('comicsansms',25)
text = smallfont.render('quit', True, (255,00,255))
color_light = (255,255,255)
color_dark = (0,0,0)
# Run until the user asks to quit

#green_button = button( 519, 281, 273,53, 'Start Game',(0,255,0))
#quit_button = button( width/2+50, height/2, 250, 100,"click me",(255, 0, 255))

start_button = button(width/2.807,height/1.50313,20,100,'',None,"imgs/buttons/slice_start.png","imgs/buttons/hovering_slice_start.png")
quit_button = button(width/2.2980,height/1.26760,20,100,'',None,"imgs/buttons/slice_quit.png", "imgs/buttons/hovering_slice_quit.png")
audio_button = button(width/2.015748,height/1.09923,20,100,'',None,"imgs/buttons/slice_audio.png", "imgs/buttons/hovering_slice_audio.png")
accessibility_button = button(width/2.3063063,height/1.09923,20,100,'',None,"imgs/buttons/slice_cb.png", "imgs/buttons/hovering_slice_cb.png")

notify_msg = button( width/2+50, height/2, 250, 100,"PRESS ENTER TO GO BACK TO MAIN MENU FOR NOW",(255, 0, 255), None, None)

# xIMG,yIMG= 400, 100

continue_button = button(width/2.4288,height/2.1951219, 20, 100, '', None, "imgs/buttons/slice_continue.png","imgs/buttons/hovering_slice_continue.png",160)
restart_button = button(width/2.4015,height/1.75182, 20, 100, '', None, "imgs/buttons/slice_restart.png","imgs/buttons/hovering_slice_restart.png",160)
tutorial_button = button(width/2.424242,height/1.50627, 20, 100, '', None, "imgs/buttons/slice_tutorial.png","imgs/buttons/hovering_slice_tutorial.png",160)
pause_title = button(width/3.12195,height/11.6129, 20, 100, '', None, "imgs/slice_paused.png","imgs/slice_paused.png",160) #bad code 


running = True
main_menu = True
pause_menu = False
in_game = False
while running:
    if main_menu:
        drawMainMenu()
        # screen.fill((40, 0, 80))
        # Did the user click the window close button?
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isOver(mouse):
                    print("start pressed")
                    main_menu = False
                    in_game = True
                if quit_button.isOver(mouse):
                    pygame.quit()
            # if event.type == pygame.MOUSEMOTION:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # print("width: " + str(width/mouse[0]))
                    # print("height: " + str(height/mouse[1]))
                    print(mouse)
    elif not main_menu and not pause_menu and in_game:
        #screen.fill((40, 0, 80))
        notify_msg.draw(screen)
        #print("we are supposed to be in game right now.")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu = True
                if event.key == pygame.K_RETURN:
                    main_menu = True
    else:
        drawPauseMenu()
        # pause_title = button(xIMG,yIMG, 20, 100, '', None, "imgs/slice_paused.png","imgs/slice_paused.png",160)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.isOver(mouse):
                    print("test")
                    main_menu = False
                    pause_menu = False
                    in_game = True
                if quit_button.isOver(mouse):
                    pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # go back to game
                    pause_menu = False
                    main_menu = False
                    in_game = True
            
                #for finding location of button
                # if event.key == pygame.K_RIGHT:
                #     xIMG = xIMG+1
                # if event.key == pygame.K_LEFT:
                #     xIMG = xIMG-1
                # if event.key == pygame.K_DOWN:
                #     yIMG = yIMG+1
                # if event.key == pygame.K_UP:
                #     yIMG = yIMG-1
                # if event.key == pygame.K_RETURN:
                #     print("x: " +str(xIMG) + " y: " +str(yIMG))
                # if event.key == pygame.K_SPACE:
                #     # print("width: " + str(width/mouse[0]))
                #     # print("height: " + str(height/mouse[1]))
                #     print(pygame.mouse.get_pos())


    # Fill the background with white
    
    
    # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
    #         pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
            
    # else:
    #     pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
    # screen.blit(text , (width/2+50,height/2))
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
