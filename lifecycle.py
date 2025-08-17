from lib.scene import add_obj

class GameState:
    def __init__(self, is_running, scene):
        self.is_running = is_running
        self.scene = scene

game_state = GameState(True, None)

