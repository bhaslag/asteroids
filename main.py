import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  running = True
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

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    screen.fill((0, 0, 0))

    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.collide_with(player):
        print("Player hit by asteroid!")
        print("Game over!")
        running = False
      
      for shot in shots:
        if shot.collide_with(asteroid):
          asteroid.split()
          shot.kill()

    for obj in drawable:
      obj.draw(screen)
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()