import pygame
from sys import exit

IS_MAIN_MENU = True
is_in_game = False
is_game_paused = False

pygame.init()
screen = pygame.display.set_mode((800,400), pygame.RESIZABLE)
pygame.display.set_caption('Break the Bank')



clock = pygame.time.Clock()

def main_menu():

    #image surface  
    main_menu_image = pygame.image.load('main_menu_image.png').convert_alpha()
    main_menu_image = pygame.transform.scale(main_menu_image, (1280,720))

    screen_pos_x, screen_pos_y = screen.get_size()

    main_menu_image = pygame.transform.scale(main_menu_image, (screen_pos_x,screen_pos_y))

    screen.blit(main_menu_image,(0,0))
    play_game_button_rect = createButton ('Pixeltype.ttf', 50, 'Play Game', 'Black', screen_pos_x/2, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and play_game_button_rect.collidepoint((event.pos)):
            print("From main menu play game")
            screen.fill('White')
            
            global IS_MAIN_MENU
            IS_MAIN_MENU = False

            global is_in_game
            is_in_game = True
            return
           
def in_game():
    sky_surf = pygame.image.load('Sky.png').convert_alpha()
    ground_surf = pygame.image.load('ground.png').convert_alpha()

    ground_value = 305

    player1_surf = pygame.image.load('red_hat_standing.png')
    player1_rect = player1_surf.get_rect(midbottom = (80,ground_value))
    player1_gravity = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w and player1_rect.bottom >= 300:
                player1_gravity = -10

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            player1_rect.right += 2
        if keys[pygame.K_a]:
            player1_rect.left -= 2

        player1_gravity+= 1
        player1_rect.y += player1_gravity

        if player1_rect.bottom >= ground_value:
            player1_rect.bottom = ground_value

        if player1_rect.left <= 2:
            player1_rect.left = 2

        if player1_rect.right >= 798:
            player1_rect.right = 798

        screen.blit(ground_surf, (0,300))
        screen.blit(sky_surf, (0,0))
        screen.blit(player1_surf,player1_rect)
        
        pygame.display.update()
        clock.tick(60)

def createButton(font_path, font_size, button_text, color, x_pos, y_pos): #returns a button

    button_font = pygame.font.Font(font_path, font_size)
    button_surf = button_font.render(button_text, False, color)
    button_rect = button_surf.get_rect(center = (x_pos,y_pos))

    screen.blit(button_surf, button_rect)

    return button_rect





while True:
    
    if IS_MAIN_MENU is True:
        print(IS_MAIN_MENU)
        main_menu()
        pygame.display.update()
        clock.tick(60)

    else:
        pygame.display.update()
        clock.tick(60)
        break
    
if is_in_game:
    in_game()


pygame.display.update()
clock.tick(60)