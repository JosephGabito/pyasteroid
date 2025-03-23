import pygame

class Score():
    
    def __init__(self):
        self.points = 0;
    
    def render(self,screen):
        font = pygame.font.SysFont("Arial", 30)
        score_surface = font.render(f"Score: {self.get_points()}", True, "white")
        screen.blit(score_surface, (10, 10))
        
    def add(self,asteroid):
        self.points+=asteroid.radius
        
    def get_points(self):
        return self.points
    
    def reset(self):
        self.points = 0