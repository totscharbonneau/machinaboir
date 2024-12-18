from src.states.state import State
from src.states.selectParain import Selection
from src.elements.ui.loading import Loading


class Title(State):
    def __init__(self,game):
        State.__init__(self,game)

    def update(self,dt,actions):
        if actions["enter"]:
            new_state = Selection(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self,display):
        display.fill((255,255,255))
        self.game.draw_text(display, "love tester demo", (0,0,0), self.game.game_width/2, self.game.game_height/2)