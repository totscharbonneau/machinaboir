import pygame
import gif_pygame
import os


class Loading():
    def __init__(self, game):
        self.gif = gif_pygame.load(os.path.join(game.ui_dir, "loading.gif"))

    def update(self, dt, actions):
        pass

    def render(self, surface):
        self.gif.render(surface,(100,100))