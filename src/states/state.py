class State():
    def __init__(self,game):
        self.game = game
        self.last_state = None

    def update(self,dt,actions):
        pass

    def render(self,surface):
        pass
    
    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()