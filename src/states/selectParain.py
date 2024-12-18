from src.states.state import State
from src.states.BOIRE import Boire
from src.elements.carousel import Carousel
from src.elements.ui.coeur import Coeur


class Selection(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.caroussel = Carousel(self.game)
        self.coeur = Coeur(self.game, 790, 170, 400, 500)

    def update(self, dt, actions):
        self.caroussel.update(dt, actions)
        if actions["enter"]:
            self.game.yourSecretLoverData = self.caroussel.parrainlist[self.caroussel.selectedParrainkey].data
            new_state = Boire(self.game, self.caroussel.parrainlist[self.caroussel.selectedParrainkey].data)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "select", (0, 0, 0), self.game.game_width / 2, self.game.game_height / 8)
        self.caroussel.render(display)
        self.coeur.render(display)
