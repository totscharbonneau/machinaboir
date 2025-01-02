from src.states.state import State
from src.elements.carouselparrain import Parrain
from src.states.lovanalysis import LoveAnalysis
from src.elements.ui.speech import Speech
import time
import pygame, os


class Boire(State):
    def __init__(self, game, choosenParrainData):
        State.__init__(self, game)
        self.parrain = Parrain(game, choosenParrainData)
        self.parrain.overwriteposition(700,85)
        self.speechbuble = Speech(game, 400,0, 300, 300)
        self.countdown = 4
        self.start_time = None
        self.action_time = None
        self.did_leuka = False
        self.backgroud_3 = pygame.image.load(os.path.join(game.background_dir, "4_DECOMPTE.png")).convert_alpha()
        self.backgroud_2 = pygame.image.load(os.path.join(game.background_dir, "5_DECOMPTE.png")).convert_alpha()
        self.backgroud_1 = pygame.image.load(os.path.join(game.background_dir, "6_DECOMPTE.png")).convert_alpha()
        self.backgroud_go = pygame.image.load(os.path.join(game.background_dir, "7_DECOMPTE.png")).convert_alpha()
        self.backgroud_result = pygame.image.load(os.path.join(game.background_dir, "8_REGARDER_RESULTAT.png")).convert_alpha()
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
        # if self.countdown > 0:
        #     if self.con
        match int(self.countdown):
            case 3:
                surface.blit(self.backgroud_3, (0, 0))
            case 2:
                surface.blit(self.backgroud_2, (0, 0))
            case 1:
                surface.blit(self.backgroud_1, (0, 0))
            case 0:
                if not self.did_leuka:
                    surface.blit(self.backgroud_go, (0, 0))
                else:
                    surface.blit(self.backgroud_result, (0, 0))
                    self.game.draw_text(surface, f"{self.action_time:.3f} seconds", (0, 0, 0),
                                        self.game.game_width / 4- 10, self.game.game_height / 4 - 65 )
                    self.game.draw_text(surface, f"Press again to calculate your LOVE <3", (255, 105, 180),
                                        self.game.game_width / 2, 3 * self.game.game_height / 5 + 110)

                    self.speechbuble.render(surface)
                    self.parrain.render(surface)
                    self.game.draw_text(surface, f"Yo MEE jai fait \n {self.game.yourSecretLoverData['time']} seconds", (0, 0, 0), 550, 150)

