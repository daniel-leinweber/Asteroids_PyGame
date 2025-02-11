import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create sprite groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroidField = AsteroidField()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
