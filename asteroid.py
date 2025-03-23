from circleshape import CircleShape
from constants import *
import pygame
import random

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
        
    def split(self,dt):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            
            blue_angle = random.uniform(20,100)
            
            base_speed = self.velocity.length()
            
            vector1 = pygame.Vector2(0,base_speed).rotate(blue_angle)
            vector2 = pygame.Vector2(0,base_speed).rotate(-blue_angle)
            
            old_radius = self.radius
            smaller_asteroid = old_radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x,self.position.y, smaller_asteroid)
            asteroid2 = Asteroid(self.position.x,self.position.y, smaller_asteroid)
            
            asteroid1.velocity = self.velocity + (vector1 * 1.2)
            asteroid2.velocity = self.velocity + (vector2 * 1.2)


