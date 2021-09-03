import pygame as p
import sys
import random

p.init()
#CONSTANTS

WIDTH = 1280
HEIGHT = 960
MAX_FPS = 60

#VARS
clock = p.time.Clock()
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice ((1,-1))
opponent_speed = 7
screen = p.display.set_mode((WIDTH, HEIGHT))

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *=-1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *=-1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def opponent_ai():
    if opponent.top <ball.y:
        opponent.top+= opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH/2, HEIGHT/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

#Colors
bg_color = p.Color('grey12')
light_grey = (200,200,200)



#Rects
ball = p.Rect(WIDTH/2 - 15, HEIGHT/2 - 15,30,30)
player = p.Rect(WIDTH - 20, HEIGHT/2 - 70,10,140)
opponent = p.Rect(10, HEIGHT/2 - 70,10,140)

player_speed = 0

#Loop
running = True
while running is True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
#starts sliding movement
        if event.type == p.KEYDOWN:
            if event.key == p.K_DOWN:
                player_speed +=7
            if event.key == p.K_UP:
                player_speed -=7
#stops sliding movement
        if event.type == p.KEYUP:
                if event.key == p.K_DOWN:
                    player_speed -=7
                if event.key == p.K_UP:
                    player_speed +=7
    
    ball_animation()
    player_animation()
    opponent_ai()

    #Drawing rects
    screen.fill(bg_color)
    p.draw.rect(screen, light_grey, player)
    p.draw.rect(screen, light_grey, opponent)
    p.draw.ellipse(screen, light_grey, ball)
    p.draw.aaline(screen, light_grey, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

    
    p.display.flip()
    clock.tick(MAX_FPS)
