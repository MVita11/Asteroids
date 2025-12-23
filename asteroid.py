import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2,
        )
    def update(self, dt):
        # Asteroid movement logic can be added here
        self.position += self.velocity * dt
        
    
    def split(self):
        # Logic to split the asteroid into smaller pieces
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            log_event("asteroid_split", pos=[round(self.position.x, 2), round(self.position.y, 2)], radius=self.radius)
            random.uniform(20, 50)
            self.velocity.rotate_ip(random.uniform(-30, 30))
            self.velocity.rotate_ip(random.uniform(-30, 30))
            self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            child1.velocity = self.velocity.rotate(random.uniform(-30, 30))
            child2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            child2.velocity = self.velocity.rotate(random.uniform(-30, 30))
            return [child1, child2]    
            
        