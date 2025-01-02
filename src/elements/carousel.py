from src.parraindata import parrain_data
from src.elements.carouselparrain import Parrain

class Carousel():
    def __init__(self,game):
        self.game = game
        self.windowsize = 7
        self.parrainlist = []
        self.currentParrains = []
        self.selectedParrainkey = 0
        self.initParrains()

    def set_parrain_window(self):

        position = self.selectedParrainkey
        window_size = self.windowsize

        # Ensure the position is within the bounds of the list
        position = position % len(self.parrainlist)

        # Calculate the start and end indices of the window
        half_window = window_size // 2
        start = (position - half_window) % len(self.parrainlist)
        end = (position + half_window + 1) % len(self.parrainlist)

        # Create the window by slicing the list and wrapping around if needed
        if start < end:
            window = self.parrainlist[start:end]
        else:
            window = self.parrainlist[start:] + self.parrainlist[:end]

        self.currentParrains = window

        self.parrainlist[(start - 1) % 24].overwriteposition(-2 * (self.game.game_width / 5), self.game.game_height / 4)

        self.parrainlist[(end + 1) % 24].overwriteposition(6 * self.game.game_width / 5, self.game.game_height / 4)

    def initParrains(self):
        for parrain in parrain_data:
            self.parrainlist.append(Parrain(self.game,parrain))

        self.set_parrain_window()

        self.set_positionCurrentP(True)


    def set_positionCurrentP(self,force=False):

        mii_width = self.parrainlist[0].sprite.get_width()
        spacing = (self.game.game_width - 5 * mii_width) / (6)

        for i, live_parain in enumerate(self.currentParrains):
            offset = i - 1
            live_parain.x = spacing + offset*(spacing+mii_width)
            live_parain.y = self.game.game_height / 4

            if force:
                live_parain.real_x, live_parain.real_y = live_parain.x, live_parain.y



    def update(self, dt, actions):
        if actions['left']:
            self.selectedParrainkey = (self.selectedParrainkey - 1) % 24

        elif actions['right']:
            self.selectedParrainkey = (self.selectedParrainkey + 1) % 24

        self.set_parrain_window()
        self.set_positionCurrentP()

        for live_parain in self.currentParrains:
            live_parain.update(dt,actions)

    def render(self,display):
        for i, live_parain in enumerate(self.currentParrains):
            # if i == 3:
            #     live_parain.render(display, True)
            live_parain.render(display)

