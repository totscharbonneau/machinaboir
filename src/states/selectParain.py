from src.states.state import State
from src.states.BOIRE import Boire
from src.elements.carousel import Carousel
from src.elements.ui.coeur import Coeur
import pygame, os


class Selection(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.caroussel = Carousel(self.game)
        # self.coeur = Coeur(self.game, 100, 170, 200, 200)
        # self.coeur.center(self.game.game_width/2,200)
        self.background = pygame.image.load(os.path.join(game.background_dir, "3_CHOIX_PARRAIN.png")).convert_alpha()

    def update(self, dt, actions):
        self.caroussel.update(dt, actions)
        if actions["enter"]:
            self.game.yourSecretLoverData = self.caroussel.parrainlist[self.caroussel.selectedParrainkey].data
            new_state = Boire(self.game, self.caroussel.parrainlist[self.caroussel.selectedParrainkey].data)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background, (0, 0))
        pygame.draw.rect(display, (255, 105, 180) , (self.game.game_width/2-141/2, 120 ,141, 335),4)
        self.caroussel.render(display)
