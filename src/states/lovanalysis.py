from src.states.state import State
from src.elements.ui.pointer import LovePointer
from src.elements.ui.loveDial import LoveDial
import pygame,os
from src.states.FIN import Fin

class LoveAnalysis(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.background = pygame.image.load(os.path.join(game.background_dir, "9_COMPATIBILITE.png")).convert_alpha()
        self.timegoal = game.yourSecretLoverData["time"]
        self.urtime = game.yourLeukaTime
        self.love = self.calclove()
        self.pointer = LovePointer(game,self.calcAngle())
        self.dial = LoveDial(game,0,0,1178,698)
        self.dial.center(game.game_width/2,game.game_height/2)


    def calclove(self):
        dt = self.timegoal - self.urtime
        love = -abs(5 * dt) + 100
        if love < 0:
            love = 0
        return love

    def calcAngle(self):
        angle = self.love*1.8
        return angle
    def calcPourcent(self,angle):
        return angle/1.8
    def update(self, dt, actions):
        if actions["enter"]:
            new_state = Fin(self.game)
            new_state.enter_state()
        self.game.reset_keys()

        self.pointer.update(dt, actions)

    def render(self,surface):
        surface.blit(self.background, (0, 0))
        self.game.draw_text(surface, f"{(self.calcPourcent(self.pointer.angle)):.1f} % de LOVE ", (255, 255, 255), self.game.game_width / 2 - 170, self.game.game_height / 8 + 71)
        self.pointer.render(surface)