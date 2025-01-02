import pygame,os
import gif_pygame

class Parrain():
    def __init__(self,game,data):
        self.game = game
        self.data = data
        self.sprite = pygame.image.load(os.path.join(game.mii_dir,data["sprite"])).convert_alpha()
        self.gif = gif_pygame.load(os.path.join(game.mii_dir, "dancingmii.gif"))
        self.x ,self.y = 0 , 0
        self.real_x,self.real_y = 0 ,0
        self.speed = 800
        self.current_frame , self.last_frame_update = 0, 0

        self.font = pygame.font.Font(None, 50)
        self.text_surface = self.font.render(self.data['name'], True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.mii_width = self.sprite.get_width()
        self.text_rect.center = (self.real_x + self.mii_width / 2, self.real_y - 10)

    def update(self,dt,actions):
        if self.real_x != self.x:
            if abs(self.real_x - self.x) < self.speed*dt:
                self.real_x = self.x
            elif self.real_x < self.x:
                self.real_x += self.speed*dt
            else:
                self.real_x -= self.speed*dt
        if self.real_y != self.y:
            if abs(self.real_y - self.y) < self.speed*dt:
                self.real_y = self.y
            elif self.real_y < self.y:
                self.real_y += self.speed*dt
            else:
                self.real_y -= self.speed*dt

        self.text_rect.center = (self.real_x + self.mii_width / 2, self.real_y - 15)

    def render(self,display,gif=False):
        if gif:
            self.gif.render(display, (self.real_x,self.real_y))
        else:
            display.blit(self.sprite,(self.real_x,self.real_y))
        self.drawName(display)

    def overwriteposition(self,x,y):
        self.real_x, self.real_y = x, y
        self.x, self.y = x, y

    def drawName(self,display):
        display.blit(self.text_surface, self.text_rect)