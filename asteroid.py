import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, ("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
      
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
          return
        new_angle = random.uniform(20, 50)
        rotated_vector_one = self.velocity.rotate(new_angle)
        rotated_vector_two = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        baby_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        baby_asteroid_a.velocity = rotated_vector_one * 1.2
        baby_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        baby_asteroid_b.velocity = rotated_vector_two * 1.2