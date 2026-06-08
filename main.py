#it works for the first 5 seconds bouncing off the screen but then it starts to bug and get stuck to the side of the screen
#Space Game
import pygame
from random import randint

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid")
player_direction = -1
running = True
clock = pygame.time.Clock()

player_direction = pygame.math.Vector2(2, -1)
player_speed = 300

#surface
surf = pygame.Surface((100,200))
surf.fill("orange")
x = 100
player_surf = pygame.image.load("spacegame/images/player.png") #importing image
star_surf = pygame.image.load("spacegame/images/star.png") #importing stars
meteor_surf = pygame.image.load("spacegame/images/meteor.png")
Laser_surf = pygame.image.load("spacegame/images/laser.png")

#importing rectangle
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
#laser_rect = Laser_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
laser_rect = Laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT-20))

#creating rectangles
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

star_positions = []
for i in range(20):
    star_positions.append((randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)))
    
while running:
    #event loop
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surface.fill("darkgray") #background colour
    for pos in star_positions:
        display_surface.blit(star_surf,pos)
    if player_rect.right < WINDOW_WIDTH:
        player_rect.left += 0.1
        player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf,(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    display_surface.blit(Laser_surf, laser_rect)

    #player movement + dvd solution
    #this makes the ship bounce off the window edges like the old DVD logo.
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        player_direction.y *= -1
    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    player_rect.center += player_direction * player_speed * dt

    x += 0.1

    #these 3 snippets arent working
    #player_rect.x += player_direction * 0.4
    #if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #    player_direction *= -1
    display_surface.blit(player_surf, player_rect)
    pygame.display.update()

surf = pygame.Surface((100,200)) #display template dimensions of the imager
display_surface.blit(surf,(100,150)) #size of the surface

pygame.quit
