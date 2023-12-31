import random
import time
import pygame


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 40
        self.jump_cooldown = time.time()
        self.swing_down_cooldown = time.time()
        self.fall_speed = 3
        self.fall_cooldown = time.time()
        self.colour = random.choice(["red", "blue", "yellow", "green"])
        self.score = 0
        self.score_time = time.time()

    def update_score(self):
        if time.time() - self.score_time > 0.5:
            self.score += 1
            self.score_time = time.time()

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)

    def swing(self):
        if time.time() - self.jump_cooldown > 0.25:
            self.y -= 50
            self.jump_cooldown = time.time()
            self.fall_speed = 3

    def swing_down(self):
        if time.time() - self.swing_down_cooldown > 0.25:
            self.y += 50
            self.swing_down_cooldown = time.time()

    def fall(self):
        if time.time() - self.fall_cooldown > 0.1:
            self.fall_cooldown = time.time()
            self.fall_speed *= 1.1
            self.y += self.fall_speed


def bird_collides_with_block(bird, block):
    # Calculate the radius of the bird's bounding circle
    bird_radius = bird.size  # Assuming the bird's circle has a fixed radius

    # Calculate the coordinates of the center of the bird's bounding circle
    bird_center_x = bird.x
    bird_center_y = bird.y

    # Calculate the coordinates of the center of the block's bounding rectangle
    block_center_x = block.x + block.size / 2
    block_center_y = block.y + block.size / 2

    # Calculate the half-width and half-height of the block's bounding rectangle
    block_half_width = block.size / 2
    block_half_height = block.size / 2

    # Calculate the horizontal and vertical distances between the centers of the bird and block
    dx = abs(bird_center_x - block_center_x)
    dy = abs(bird_center_y - block_center_y)

    # Check for collision by comparing distances to the sum of radii (bird's radius + half of block's diagonal)
    if dx <= bird_radius + block_half_width and dy <= bird_radius + block_half_height:
        return True  # Collision detected
    else:
        return False  # No collision