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

    def update(self, dt):
        #input
        print(pygame.mouse.get_rel())
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self._speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print("fire laser")

        #general setup
        pygame.init()
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Asteroid")
        self.direction = -1
        running = True
        clock = pygame.time.Clock()

        self.direction = pygame.math.Vector2()
        self.speed = 300

        #surface
        surf = pygame.Surface((100,200))
        surf.fill("orange")
        x = 100

        all_sprites = pygame.sprite.Group()
        player = Player(all_sprites)

        player_surf = pygame.image.load("spacegame/images/player.png") #importing image
        star_surf = pygame.image.load("spacegame/images/star.png") #importing stars
        meteor_surf = pygame.image.load("spacegame/images/meteor.png")
        Laser_surf = pygame.image.load("spacegame/images/laser.png")

        #imports
        player_surf = pygame.image.load(join("spacegame", "images", "player.png")).convert_alpha()
        player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        laser_rect = Laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT-20))

        #creating rectangles
        player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

        star_positions = []
        for i in range(20):
            star_positions.append((randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)))
            
        while running:
            dt = clock.tick()/1000
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                #    print(1)
                #if event.type == pygame.MOUSEMOTION:
                #    player_rect.center = event.pos

            #from input to print fire laser you are meant to paste into the player class
            #input
            #print(pygame.mouse.get_rel())
            #keys = pygame.key.get_pressed()
            #player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
            #player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
            #player_direction = player_direction.normalize() if player_direction else player_direction
            #player_rect.center += player_direction * player_speed * dt

            #recent_keys = pygame.key.get_just_pressed()
            #if recent_keys[pygame.K_SPACE]:
            #    print("fire laser")


            print((self.direction * self.speed).magnitude())

            #if keys[pygame.K_RIGHT]:
            #    player_direction.x = 1
            #else:
            #    player_direction.x = 0

            #draw the game
            display_surface.fill("black") #background colour
            for pos in star_positions:
                display_surface.blit(star_surf,pos)
            if player_rect.right < WINDOW_WIDTH:
                player_rect.left += 0.1
                player_rect.center += self.direction * self.speed * dt
            display_surface.blit(player_surf, player_rect)
            display_surface.blit(meteor_surf,(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            display_surface.blit(Laser_surf, laser_rect)
            all_sprites.draw(display_surface)

            #player movement + dvd solution
            #this makes the ship bounce off the window edges like the old DVD logo.
            #if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
            #    player_direction.y *= -1
            #if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
            #    player_direction.x *= -1
            #player_rect.center += player_direction * player_speed * dt

            x += 0.1
            display_surface.blit(player_surf, player_rect)
            pygame.display.update()

        surf = pygame.Surface((100,200)) #display template dimensions of the imager
        display_surface.blit(surf,(100,150)) #size of the surface

        pygame.quit
