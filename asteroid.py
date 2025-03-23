from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):

    containers = None

    def __init__(self,x,y,radius):
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.position.x, self.position.y), self.radius)

    def update(self,dt):
        self.position += self.velocity * dt


