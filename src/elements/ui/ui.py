import pygame, os


class UI():
    def __init__(self, game, pathtosprite, x, y, w=None, h=None):
        self.game = game
        self.sprite = pygame.image.load(os.path.join(game.ui_dir, pathtosprite)).convert_alpha()
        if w is None and h is None:
            self.w = self.sprite.get_width()
            self.h = self.sprite.get_height()
        else:
            self.w, self.h = w, h
        self.x, self.y = x, y
        self.scale_sprite()

    def scale_sprite(self):
        self.sprite = pygame.transform.scale(self.sprite, (self.w, self.h))

    def center(self,x,y):
        self.x = x - self.sprite.get_width()/2
        self.y = y - self.sprite.get_height()/2


    def update(self, dt, actions):
        pass

    def render(self, surface):
        pass
