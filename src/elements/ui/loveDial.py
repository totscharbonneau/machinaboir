from src.elements.ui.ui import UI

class LoveDial(UI):
    def __init__(self, game, x, y, w=None, h=None):
        UI.__init__(self, game, "lovedial.png", x, y, w, h)

    def update(self, dt, actions):
        pass

    def render(self, surface):
        surface.blit(self.sprite, (self.x, self.y))