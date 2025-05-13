from settings import *
from functions import *

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

# checking for events
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0                         


    animate_ball()
    animate_player()
    animate_computer()      

    # clearing the screen
    screen.fill('black')

    # draw the score  
    computer_score_surface = score_font.render(str(computer_score), True, 'white')
    player_score_surface = score_font.render(str(player_score), True, 'white')     
    screen.blit(computer_score_surface, (screen_width/4, 20))
    screen.blit(player_score_surface, (3*screen_width/4, 20))
    
    # drawing game objects
    pygame.draw.aaline(screen, 'white', (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.rect(screen, 'white', computer)
    pygame.draw.rect(screen, 'white', player)
    
    # update the screen
    pygame.display.update()
    clock.tick(60)
    