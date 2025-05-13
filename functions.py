import pygame
import sys
import random
from settings import *

def reset_ball():
    global ball_speed_x, ball_speed_y
    
    ball.x = screen_width/2 -10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1]) 


def score_won(winner):
    global computer_speed, player_score
    
    if winner == "computer":
        computer_score += 1
    if winner == "player":
        player_score += 1
    reset_ball()   
    
    
def animate_ball():
    global ball_speed_x, ball_speed_y
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1
    
    if ball.right >= screen_width:
        score_won("computer")
    
    if ball.left <= screen_width:
        score_won("player")
        
    if ball.colliderect(computer) or ball.colliderect(player):
        ball_speed_x *= -1
        
        
def animate_computer():
    global computer_speed
    computer.y += computer_speed
    
    if ball.centery <= computer.centery:
        computer_speed = -6 
    
    if ball.centery >= computer.centery:
        computer_speed = 6                 
    
    if computer.top <= 0:
        computer.top = 0
    
    if computer.bottom >=screen_height:
        computer.bottom = screen_height
        

def animate_player():
    player.y = player_speed
    
    if player.top <= 0:
        player.top = 0
        
    if player.bottom >= screen_height:
        player.bottom = screen_height                                 