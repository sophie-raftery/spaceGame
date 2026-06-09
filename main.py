#Space Game
import pygame
from tkinter import font
from random import randint, uniform
from os.path import join, dirname, abspath
from operator import pos

#player class
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

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            print("fire laser")
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()

#star class
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

#laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

        self.speed = 600

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()

#meteor class
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.start_time = pygame.time.get_ticks()
        self.life_time = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)
    
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time > self.life_time:
            self.kill()

#collision function
def collisions():
    global running

    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True)
    if collision_sprites:
        running = False

    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

#display score function
def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (240, 240, 240))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (240, 240, 240), text_rect.inflate(20,10).move(0, -8), 5, 10)

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid")
running = True
clock = pygame.time.Clock()


#surfaces
#surf = pygame.Surface((100,200))

#sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join("spacegame/images/star.png")).convert_alpha()
laser_sprites = pygame.sprite.Group()

#create the 20 stars
for i in range(20):
    Star(all_sprites, star_surf)

player = Player(all_sprites)

#imports
star_surf = pygame.image.load(join("spacegame/images/star.png")).convert_alpha()
meteor_surf = pygame.image.load(join("spacegame/images/meteor.png")).convert_alpha()
laser_surf = pygame.image.load(join("spacegame/images/laser.png")).convert_alpha()
font = pygame.font.Font(join("spacegame/images/Oxanium-Bold.ttf"), 20)
text_surf = font.render("text", True, (240, 240, 240))

# player_surf = pygame.image.load(join("spacegame", "images", "player.png")).convert_alpha()
# player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
#laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT-20))

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
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))

    #draw the game, whatever is drawn last sits on top
    display_surface.fill("black") #background colour
    all_sprites.draw(display_surface)
    display_score()

    all_sprites.update(dt)
    collisions()

    pygame.display.update()

pygame.quit
