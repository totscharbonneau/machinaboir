from src.elements.ui.ui import UI


class Coeur(UI):
    def __init__(self, game, x, y, w, h):
        UI.__init__(self, game, "coeur.png", x, y, w, h)

    def update(self, dt, actions):
        pass

    def render(self, surface):
        surface.blit(self.sprite, (self.x, self.y))
