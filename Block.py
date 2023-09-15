import time


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 40
        self.move_time = time.time()
        self.move_cooldown = 0.1

    def move(self):
        if time.time() - self.move_time > self.move_cooldown:
            self.x -= 1
