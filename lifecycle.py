from lib.io import parse_phyobj
from lib.scene import add_obj
import os

class GameState:
    def __init__(self, is_running, scene):
        self.is_running = is_running
        self.scene = scene

game_state = GameState(True, None)

RES = 'src/res/'


def build_objs():
    pass
