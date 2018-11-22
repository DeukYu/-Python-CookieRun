import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None
    bg = None

    def __init__(self, bg):
        if Ball.bg == None:
            Ball.bg = bg
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(150, 1600 - 1), random.randint(100, 1000 - 1), 0

    def get_bb(self):
        return self.x - self.bg.window_left - 10, self.y - self.bg.window_bottom - 10, self.x - self.bg.window_left + 10, self.y - self.bg.window_bottom + 10

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

