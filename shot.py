import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from logger import log_event

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        # initialize velocity from direction so shots are usable immediately
        self.velocity = direction * PLAYER_SHOOT_SPEED
        # log creation for telemetry/tests
        log_event("asteroid_shot", pos=[round(self.position.x, 2), round(self.position.y, 2)], vel=[round(self.velocity.x, 2), round(self.velocity.y, 2)])

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "red",
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )