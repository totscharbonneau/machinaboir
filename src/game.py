import sys,os, time, pygame

from src.states.title import Title
import serial

class Game():
    def __init__(self):
        pygame.init()
        self.game_width, self.game_height = 960, 510
        self.screen_width, self.screen_height = 1980/1.5, 1020/1.5
        self.game_canvas = pygame.Surface((self.game_width, self.game_height))
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.inputs = {"left":False,"right":False,"enter":False,"valve":False}
        self.yourSecretLoverData = None
        self.yourLeukaTime = None
        self.running = True
        self.dt, self.prez_time = 0, 0
        self.state_stack = []
        self.load_assets()
        self.start_states()
        self.serial_connection = serial.Serial("COM3", 9600, timeout=1)

    def get_serial_events(self):
        # Read serial data from Arduino
        if self.serial_connection.in_waiting > 0:
            line = self.serial_connection.readline().decode("utf-8").strip()
            print(line)
            if line == "Select":
                self.inputs["enter"] = True
            elif line == "Left":
                self.inputs["left"] = True
            elif line == "Right":
                self.inputs["right"] = True


    def game_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            clock.tick(60)

        pygame.quit()  # Quit Pygame and close the window cleanly

    def get_events(self):
        self.get_serial_events()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # changer pour les boutons
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        self.inputs["left"] = True
                    case pygame.K_RIGHT:
                        self.inputs["right"] = True
                    case pygame.K_SPACE:
                        self.inputs["enter"] = True
                    case _:
                        print("keydown case not specified")
            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT:
                        self.inputs["left"] = False
                    case pygame.K_RIGHT:
                        self.inputs["right"] = False
                    case pygame.K_SPACE:
                        self.inputs["enter"] = False
                    case _:
                        print("keydown case not specified")

    def update(self):
        self.state_stack[-1].update(self.dt,self.inputs)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.screen_width,self.screen_height)),(0,0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prez_time
        self.prez_time = now

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.mii_dir = os.path.join(self.assets_dir,"parrainmii")
        self.ui_dir = os.path.join(self.assets_dir,"ui")
        self.background_dir = os.path.join(self.assets_dir,"background")
        self.font = pygame.font.Font(None,40)

    def draw_text(self,surface,text,color,x,y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface,text_rect)

    def start_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.inputs:
            self.inputs[action] = False