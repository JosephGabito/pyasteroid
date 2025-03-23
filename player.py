from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame

class Player(CircleShape):
    
    containers = None
    timer = 0
    
    def __init__(self,x,y):
        
        self.ship_img = pygame.image.load("assets/spaceship02.png").convert_alpha()
        self.ship_img = pygame.transform.scale(self.ship_img, (50, 50))

        self.shot_laser_sound = pygame.mixer.Sound("sounds/shot-laser.wav")
        
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 180
    
    def triangle(self):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    def draw(self,screen):
       # pygame.draw.polygon(screen, 'white', self.triangle(), 2)
        rect = self.ship_img.get_rect(center=(self.position.x, self.position.y))
        rotated_image = pygame.transform.rotate(self.ship_img, -self.rotation)
        screen.blit(rotated_image, rect)
        
    def move_up(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def move_down(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position -= forward * PLAYER_SPEED * dt

    def rotate_right(self,dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360
    
    def rotate_left(self,dt):
        self.rotation = (self.rotation - PLAYER_TURN_SPEED * dt) % 360

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer = self.timer - dt
        
        if keys[pygame.K_a]:
            self.rotate_left(dt)
        if keys[pygame.K_d]:
            self.rotate_right(dt)
        if keys[pygame.K_w]:
            self.move_up(dt)
        if keys[pygame.K_s]:
            self.move_down(dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0: # Cooldown
                self.shoot()
    
    def shoot(self):
        self.timer = PLAYER_SHOOT_COOLDOWN
        direction_vector = pygame.Vector2(0, 1)
        rotated_vector = direction_vector.rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS )
        shot.velocity = (shot.velocity + rotated_vector) * PLAYER_SHOOT_SPEED
        self.shot_laser_sound.play()



