from src.states.state import State
import pygame
import os, sys

class Fin(State):
    def __init__(self,game):
        State.__init__(self,game)
        self.background = pygame.image.load(os.path.join(game.background_dir, "11_FIN.png")).convert_alpha()

    def update(self,dt,actions):
        if actions["enter"]:
            self.game.running = False
        self.game.reset_keys()

    def render(self,display):
        display.blit(self.background, (0, 0))