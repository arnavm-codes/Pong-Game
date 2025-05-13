import pygame
pygame.init()
# Game screen dimensions
screen_width = 1280
screen_height = 800

# pong ball dimensions and position
ball = pygame.Rect(0,0,30,30)
ball.center = (screen_width/2, screen_height/2)

# computer player dimensions
computer = pygame.Rect(0,0,20,100)
computer.centery = screen_height/2

# user player dimensions
player = pygame.Rect(0,0,20,100)
player.midright = (screen_width, screen_height/2)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
computer_speed = 6

computer_score, player_score = 0, 0

score_font = pygame.font.Font(None, 100)
