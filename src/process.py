from lib.prompt import change_prompt
from lib.camera import draw_viewport
from src.ui import draw_frame
from src.ui import draw_hp_bar
from src.ui import draw_inventory
from src.ui import draw_actions
from lifecycle import game_state


class Player:
    def __init__(self, position=(0, 0), sprite='.'):
        self.x, self.y= position
        self.sprite = sprite

    def get(self):
        return (self.x, self.y), self.sprite


player = Player((10, 4), 'Y')


def init_game():
    change_prompt('Y->==> ')


def destroy_game():
    pass


from lib.camera import obj1

def draw_process():
    draw_frame()
    draw_hp_bar((18, 1), 3)
    draw_inventory((18, 3), *['->==>', '[DDD]', 'o--++', None])
    draw_actions((0, 9), "{'a'-left, 's'-down, 'w'-up, 'd'-right, 'dtw'-destroy this world}")
    draw_viewport((1, 1), (13, 7), obj1)


def input_process(action):
    if action == 'dtw':
        game_state.is_running = False

    match action:
        case 'a':
            player.x -= 1
            obj1.x -= 1
        case 'd':
            player.x += 1
            obj1.x += 1
        case 'w':
            player.y -= 1
            obj1.y -= 1
        case 's':
            player.y += 1
            obj1.y += 1
