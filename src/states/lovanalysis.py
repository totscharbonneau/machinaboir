from src.states.state import State
from src.elements.ui.pointer import LovePointer
from src.elements.ui.loveDial import LoveDial

class LoveAnalysis(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.timegoal = game.yourSecretLoverData["time"]
        self.urtime = game.yourLeukaTime
        self.love = self.calclove()
        self.pointer = LovePointer(game,self.calcAngle())
        self.dial = LoveDial(game,0,0,1178,698)
        self.dial.center(game.game_width/2,game.game_height/2)


    def calclove(self):
        dt = self.timegoal - self.urtime
        love = -abs(10 * dt) + 100
        if love < 0:
            love = 0
        return love

    def calcAngle(self):
        angle = self.love*1.8
        return angle
    def update(self, dt, actions):
        self.pointer.update(dt, actions)

    def render(self,surface):
        surface.fill((255, 255, 255))
        self.game.draw_text(surface, "LOVE ANALYSIS", (0, 0, 0), self.game.game_width / 2, self.game.game_height / 8)
        self.dial.render(surface)
        self.pointer.render(surface)