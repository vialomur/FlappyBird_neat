import pygame
from Bird import *
from Block import *
import time
import random


# Create a function to add a new block
def add_block():
    y = random.randint(10, HEIGHT - 40)  # Randomize the block's vertical position
    new_block = Block(WIDTH, y)
    blocks.append(new_block)


# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

bird = Bird(200, HEIGHT // 2)
time_start = time.time()
block_respawn_time = 1
blocks = []
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", (bird.x, bird.y), bird.size)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bird.swing()

    if keys[pygame.K_s]:
        bird.swing_down()

    bird.fall()

    if bird.y <= 0:
        bird.y = 0

    if bird.y >= HEIGHT - bird.size:
        bird.y = HEIGHT - bird.size
        bird.fall_speed = 3

    # Add new blocks at regular intervals
    if time.time() - time_start > block_respawn_time:
        add_block()
        time_start = time.time()

    # Move and draw blocks
    for block in blocks:
        block.move()
        pygame.draw.rect(screen, "green", (block.x, block.y, block.size, block.size))
        if block.x <= 0:
            blocks.remove(block)

    # Check for collisions between the bird and blocks
    for block in blocks:
        if bird_collides_with_block(bird, block):
            running = False  # Game over logic
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
