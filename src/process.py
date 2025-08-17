from lib.prompt import change_prompt
from lib.viewport import draw_viewport
from lib.viewport import Mesh
from lib.viewport import Camera
from lib.physics import detect_col
from lib.physics import move_and_collide
from lib.physics import ColBox
from lib.scene import add_obj
from lib.scene import get_obj
from lib.scene import get_scene
from lib.phyobj import PhyObj
from lib.ui import draw_frame
from lib.ui import draw_hp_bar
from lib.ui import draw_inventory
from lib.ui import draw_actions
from lifecycle import game_state
from lib.io import parse_phyobj

def init_game():
    change_prompt('Y->==> ')

    RES = 'src/res/'

    player = parse_phyobj(RES, 'player.phyobj')

    obstacle = parse_phyobj(RES, 'obstacle.phyobj')
    obstacle.pos_x = 3
    obstacle.pos_y = 3

    obstacle1 = parse_phyobj(RES, 'obstacle.phyobj')
    obstacle1.pos_x = 6
    obstacle1.pos_y = 5

    add_obj('player', player)
    add_obj('obstacle', obstacle)
    add_obj('obstacle1', obstacle1)


def destroy_game():
    pass


camera = Camera(0, 0)

import lib.render
def log(pos, **kwds):
    s = '; '.join([str((kw, kwds[kw])) for kw in kwds])
    
    for i in range(len(s)):
        lib.render.draw(i, 10 + pos, s[i])


class Any:
    def __init__(self, value):
        self.value = value


def draw_process():
    draw_frame()
    draw_hp_bar((18, 1), 3)
    draw_inventory((18, 3), *['->==>', '[DDD]', 'o--++', None])
    draw_actions((0, 9), "a | s | w | d")
    draw_viewport((1, 1), (13, 7), camera, *get_scene().values())


direction = [0, 0]

def physics_process():
    player = get_obj('player')
    
    move_and_collide(player)

    cam_follow_l = player.pos_x < 2 + camera.x and player.velocity.x < 0
    cam_follow_r = player.pos_x > 11 + camera.x and player.velocity.x > 0
    cam_follow_u = player.pos_y < 2 + camera.y and player.velocity.y < 0
    cam_follow_d = player.pos_y > 5 + camera.y and player.velocity.y > 0
    
    if cam_follow_l or cam_follow_r:
        camera.x += player.velocity.x
    if cam_follow_u or cam_follow_d:
        camera.y += player.velocity.y

    player.velocity.x = 0
    player.velocity.y = 0


def input_process(action):
    if action == 'dtw':
        game_state.is_running = False

    player = get_obj('player')
    match action:
        case 'a':
            player.velocity.x = -1
        case 'd':
            player.velocity.x = 1
        case 'w':
            player.velocity.y = -1
        case 's':
            player.velocity.y = 1
