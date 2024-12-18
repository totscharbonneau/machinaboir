from src.states.state import State
from src.elements.carouselparrain import Parrain
from src.states.lovanalysis import LoveAnalysis
import time


class Boire(State):
    def __init__(self, game, choosenParrainData):
        State.__init__(self, game)
        self.parrain = Parrain(game, choosenParrainData)
        self.countdown = 3
        self.start_time = None
        self.action_time = None
        self.did_leuka = False

    def update(self, dt, actions):
        if self.countdown > 0:
            self.countdown -= dt
            if self.countdown <= 0:
                self.countdown = 0
                self.start_time = time.time()
        else:
            if not self.did_leuka and actions['enter']:
                self.action_time = time.time() - self.start_time
                self.game.yourLeukaTime = self.action_time
                self.did_leuka = True
            elif self.did_leuka and actions['enter']:
                new_state = LoveAnalysis(self.game)
                new_state.enter_state()

        self.game.reset_keys()

    def render(self, surface):
        surface.fill((255, 255, 255))
        if self.countdown > 0:
            self.game.draw_text(surface, str(int(self.countdown) + 1), (0, 0, 0), self.game.game_width / 2,
                                self.game.game_height / 2)
        elif not self.did_leuka:
            self.game.draw_text(surface, "Go!", (0, 0, 0), self.game.game_width / 2, self.game.game_height / 2)
        elif self.action_time is not None:
            self.game.draw_text(surface, f"Ton leuka time: {self.action_time:.3f} seconds", (0, 0, 0),
                                self.game.game_width / 2, self.game.game_height / 4)
            self.game.draw_text(surface, f"Press button to analyse your love", (0, 0, 0),
                                self.game.game_width / 2, 3*self.game.game_height / 5)