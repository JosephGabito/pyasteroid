import pygame,sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
import random

stars = [{"x": random.randint(0, SCREEN_HEIGHT), "y": random.randint(0, SCREEN_WIDTH)} for _ in range(100)]

def update_stars():
    for star in stars:
        star["y"] += 1
        if star["y"] > SCREEN_HEIGHT:
            star["y"] = random.randint(0, SCREEN_HEIGHT)
            star["x"] = random.randint(0, SCREEN_WIDTH)

def draw_stars( screen ):
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (star["x"], star["y"]), 1)

def main():
    
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    explosion_sound  = pygame.mixer.Sound("sounds/explosion.wav")
    impact_sound     = pygame.mixer.Sound("sounds/impact.wav")
        
    pygame.display.set_caption("Asteroids version 0.0.1 by Joseph Gabito")
    
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    
    background = pygame.image.load("assets/parallax.png").convert()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0 # Stands for Delta time.
    
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()
    
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,drawable, updatable)
    Player.containers = (updatable,drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2) #Middle of the screen.
    player.draw(screen)

    score = Score()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Clear the screen
        screen.fill("#121212")
        score.render(screen)
        
        update_stars()
        draw_stars(screen)
        
        # Update the updatable, then redraw it
        updatable.update(dt)

        for thing in drawable:
            thing.draw(screen)
        
        for asteroid in asteroids:
            # Bullet collision
            for bullet in shots:
                if bullet.collided(asteroid):
                    score.add(asteroid)
                    asteroid.split(dt)
                    impact_sound.play()
                    
            # Player collision
            if asteroid.collided(player):
                explosion_sound.play()
                print('Game over!')
                pygame.time.delay(3000)
                sys.exit()

      

        # Swap display buffers
        pygame.display.flip()

         # Update delta time
        time_passed = clock.tick(MAX_FPS)  # Pauses the game loop to maintain 60 FPS
        dt = time_passed / 1000  # Converts ms to seconds

if __name__ == "__main__":
    main()
