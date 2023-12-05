import pygame
import sys
import random
from pygame.locals import QUIT

# Constants
WIDTH, HEIGHT = 600, 400
PARTICLE_RADIUS = 5
BALL_RADIUS = 20
FPS = 60

# Particle class
class Particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Particle-wall collision
        if self.x <= 0 or self.x >= WIDTH:
            self.vx = -self.vx
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy = -self.vy

        # Particle-ball collision
        distance = ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5
        if distance <= PARTICLE_RADIUS + BALL_RADIUS:
            # Simple collision response - reverse particle velocity
            self.vx = -self.vx
            self.vy = -self.vy

            # Update ball's velocity based on the particle's momentum
            ball.vx += self.vx
            ball.vy += self.vy

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")

# Create stationary ball
ball = Particle(WIDTH // 2, HEIGHT // 2, 0, 0)

# Create particles
num_particles = 20
particles = [Particle(
    random.randint(PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS),
    random.randint(PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS),
    random.uniform(-2, 2),
    random.uniform(-2, 2)
) for _ in range(num_particles)]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update particles
    for particle in particles:
        particle.move()

    # Update ball (optional)
    ball.move()

    # Draw everything
    screen.fill((255, 255, 255))

    # Draw particles
    for particle in particles:
        pygame.draw.circle(screen, (0, 0, 255), (int(particle.x), int(particle.y)), PARTICLE_RADIUS)

    # Draw ball
    pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)
