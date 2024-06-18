import pygame
import random
import math

# screen dimensions
WIDTH, HEIGHT = 1260,670

# boid parameters
BOID_COUNT = 50
BOID_SIZE = 5
BOID_SPEED = 2
VIEW_RADIUS = 50
SEPARATION_RADIUS = 20
SEPARATION_FORCE = 0.05
ALIGNMENT_FORCE = 0.05
COHESION_FORCE = 0.01

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * BOID_SPEED
        self.acceleration = pygame.Vector2(0, 0)

    def update(self):
        self.velocity += self.acceleration
        self.velocity = self.velocity.normalize() * BOID_SPEED
        self.position += self.velocity
        self.acceleration = pygame.Vector2(0, 0)

        # wrap around the screen edges
        if self.position.x > WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIDTH
        if self.position.y > HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = HEIGHT

    def apply_force(self, force):
        self.acceleration += force

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, BOID_SIZE)

    def separation(self, boids):
        steer = pygame.Vector2(0, 0)
        count = 0
        for boid in boids:
            distance = self.position.distance_to(boid.position)
            if 0 < distance < SEPARATION_RADIUS:
                diff = self.position - boid.position
                diff = diff.normalize() / distance
                steer += diff
                count += 1
        if count > 0:
            steer /= count
        if steer.length() > 0:
            steer = steer.normalize() * BOID_SPEED - self.velocity
        return steer * SEPARATION_FORCE

    def alignment(self, boids):
        steer = pygame.Vector2(0, 0)
        count = 0
        for boid in boids:
            if self.position.distance_to(boid.position) < VIEW_RADIUS:
                steer += boid.velocity
                count += 1
        if count > 0:
            steer /= count
            steer = steer.normalize() * BOID_SPEED
            steer -= self.velocity
        return steer * ALIGNMENT_FORCE

    def cohesion(self, boids):
        center_of_mass = pygame.Vector2(0, 0)
        count = 0
        for boid in boids:
            if self.position.distance_to(boid.position) < VIEW_RADIUS:
                center_of_mass += boid.position
                count += 1
        if count > 0:
            center_of_mass /= count
            steer = center_of_mass - self.position
            if steer.length() > 0:
                steer = steer.normalize() * BOID_SPEED
                steer -= self.velocity
                return steer * COHESION_FORCE
        return pygame.Vector2(0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Boid Simulation")
    clock = pygame.time.Clock()

    boids = [Boid(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(BOID_COUNT)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for boid in boids:
            separation_force = boid.separation(boids)
            alignment_force = boid.alignment(boids)
            cohesion_force = boid.cohesion(boids)

            boid.apply_force(separation_force)
            boid.apply_force(alignment_force)
            boid.apply_force(cohesion_force)
            boid.update()
            boid.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
