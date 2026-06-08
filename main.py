#Space Game
import pygame
from random import randint
from os.path import join, dirname, abspath

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("spacegame/images/player.png").convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 300

        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print("fire laser")
            self.can_shoot = False #in the workingWithTime doc Step 4 it says = false but i put a capital F
            self.laser_shoot_time = pygame.time.get_ticks()

#this is where i was very last left off
#document WorkingWithTimeInstruction
#top of page 5/9



class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid")
running = True
clock = pygame.time.Clock()


#surface
surf = pygame.Surface((100,200))
surf.fill("orange")
x = 100

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join("spacegame/images/star.png")).convert_alpha()

#create the 20 stars
for i in range(20):
    Star(all_sprites, star_surf)

player = Player(all_sprites)

meteor_surf = pygame.image.load(join("spacegame/images/meteor.png")).convert_alpha()
laser_surf = pygame.image.load(join("spacegame/images/laser.png")).convert_alpha()

#imports
# player_surf = pygame.image.load(join("spacegame", "images", "player.png")).convert_alpha()
# player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT-20))

#custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    dt = clock.tick()/1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #check for meteor event
        if event.type == meteor_event:
            print("create meteor")
    all_sprites.update(dt)

    #draw the game
    display_surface.fill("black") #background colour
    all_sprites.draw(display_surface)
    # display_surface.blit(meteor_surf, meteor_rect)
    # display_surface.blit(laser_surf, laser_rect)
    pygame.display.update()

pygame.quit
