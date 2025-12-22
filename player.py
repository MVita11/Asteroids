import pygame
import constants
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0  # in degrees
        self.rotate = 0  # -1 for left, 1 for right, 0 for no rotation
        self.position = pygame.Vector2(x, y)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate = -1
        if keys[pygame.K_d]:
            self.rotate = 1
        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            self.rotate = 0
        
        self.rotation += self.rotate * constants.PLAYER_TURN_SPEED * dt
        
        print(f"Debug: rotation={self.rotation}, rotate={self.rotate}, dt={dt}")
        
        self.move(dt)
        
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        