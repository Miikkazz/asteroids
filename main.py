import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
import sys
from shooting import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))  # Fill the screen with black
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
