from src.states.state import State
from src.states.selectParain import Selection

import pygame
import os

class Intro(State):
    def __init__(self,game):
        State.__init__(self,game)
        self.background = pygame.image.load(os.path.join(game.background_dir, "2_INTRO.png")).convert_alpha()

    def update(self,dt,actions):
        if actions["enter"]:
            new_state = Selection(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self,display):
        display.blit(self.background, (0, 0))