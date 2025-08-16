from lib.io import build_obj
from lib.scene import add_obj
import os

class GameState:
    def __init__(self, is_running, scene):
        self.is_running = is_running
        self.scene = scene

game_state = GameState(True, None)

RES = 'src/res/'


def build_objs():
    obj = build_obj(RES, 'obstacle.dungeon')
    add_obj('obstacle2', obj)
