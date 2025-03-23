# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids!")
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0 # Stands for Delta time.
    
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    AsteroidField.containers = (updatable,)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2) #Middle of the screen.
    player.draw(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Clear the screen
        screen.fill("#121212")
        # Update the updatable, then redraw it
        updatable.update(dt)

        for thing in drawable:
            thing.draw(screen)
        
        # Swap display buffers
        pygame.display.flip()
        
         # Update delta time
        time_passed = clock.tick(60)  # Pauses the game loop to maintain 60 FPS
        dt = time_passed / 1000  # Converts ms to seconds

if __name__ == "__main__":
    main()
