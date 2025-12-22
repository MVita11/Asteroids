import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    
    
    while True:
        log_state()
        dt = clock.tick(60) / 1000  # Delta time in seconds.
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update with dt so sprites get the time delta
        updatable.update(dt)

        # clear screen first
        screen.fill("black")

        # pass screen into draw
        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)

        # if player is not in drawable: draw explicitly, otherwise omit
        # player.draw(screen)

        pygame.display.flip()
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

if __name__ == "__main__":
    main()

