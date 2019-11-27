import pygame

pygame.init()

display_width = 1600
display_height = 900

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dog race")

bg_image = pygame.image.load("pictures/running_track.png").convert()
window.blit(bg_image, [0, 0])
dog1_image = pygame.image.load("pictures/dog1.png")
dog2_image = pygame.image.load("pictures/dog2.png")

def exit_game():
    pygame.quit()
    exit()

def dog(dog_image, x, y):
    window.blit(dog_image, (x, y))

def message_display(winner):
    text_font = pygame.font.Font("freesansbold.ttf", 115)
    text = text_font.render("The winner is " + winner + "!", True, (0, 255, 0), (0, 0, 128))
    text_rect = text.get_rect()
    text_rect.center = ((display_width/2), (display_height/2))
    window.blit(text, text_rect)
    
    #pygame.mixer.music.load("music/ff7_victory.mp3")
    #pygame.mixer.music.play()

    #exit_game()

def game_loop():
    x1 = (display_width * 0.01)
    y1 = (display_height * 0.56)
    x2 = (display_width * 0.01)
    y2 = (display_height * 0.375)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            
            if(event.type == pygame.KEYDOWN and (x1 < 1160 and x2 < 1160)):
                if event.key == pygame.K_SPACE:
                    x1 += 50
            
            if(event.type == pygame.KEYDOWN and (x1 < 1160 and x2 < 1160)):
                if event.key == pygame.K_RETURN:
                    x2 += 150

            dog(dog1_image, x1, y1)
            dog(dog2_image, x2, y2)
            
            pygame.display.update()
            window.blit(bg_image, [0, 0])

        if(x1 >= 1160):
            message_display("the red dog")
        if(x2 >= 1160):
            message_display("the blue dog")

game_loop()
