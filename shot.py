import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    
    containers = None

    def __init__(self,x,y,radius):
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", (self.position.x, self.position.y), self.radius)

    def update(self,dt):
        self.position += self.velocity * dt