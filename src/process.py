from lib.prompt import change_prompt
from lib.viewport import draw_viewport
from lib.viewport import Mesh
from lib.viewport import Camera
from lib.physics import detect_col
from lib.physics import ColBox
from lib.gameobj import PhyObj
from lib.ui import draw_frame
from lib.ui import draw_hp_bar
from lib.ui import draw_inventory
from lib.ui import draw_actions
from lifecycle import game_state


def init_game():
    change_prompt('Y->==> ')


def destroy_game():
    pass


player = PhyObj(
    mesh=Mesh((2, 2), [['Y']]),
    col_box=ColBox(2, 2, 1, 1)
)

obstacle = PhyObj(
    mesh=Mesh(
        (3, 3),
        [
            ['*', '.', '.', '*'],
            ['.', '.', '*', '.'],
            ['.', '*', '.', '.'],
            ['*', '.', '.', '*'],
        ]
    ),
    col_box=ColBox(3, 3, 4, 4)
)

obstacle1 = PhyObj(
    mesh=Mesh(
        (6, 6),
        [
            ['*', '.', '.', '*'],
            ['.', '.', '*', '.'],
            ['.', '*', '.', '.'],
            ['*', '.', '.', '*'],
        ]
    ),
    col_box=ColBox(6, 6, 4, 4)
)

camera = Camera(0, 0)

import lib.render
def log(pos, **kwds):
    s = '; '.join([str((kw, kwds[kw])) for kw in kwds])
    
    for i in range(len(s)):
        lib.render.draw(i, 10 + pos, s[i])


class Any:
    def __init__(self, value):
        self.value = value


col = Any((False, 'no_col'))

phy_obs = [
    obstacle,
    obstacle1,
]

def draw_process():
    draw_frame()
    draw_hp_bar((18, 1), 3)
    draw_inventory((18, 3), *['->==>', '[DDD]', 'o--++', None])
    draw_actions((0, 9), "{'a'-left, 's'-down, 'w'-up, 'd'-right, 'dtw'-destroy this world}")
    draw_viewport((1, 1), (13, 7), camera, player.mesh, obstacle.mesh)
    log(1, x=player.mesh.x, y=player.mesh.y, collides=col.value)


direction = [0, 0]


def move_and_collide():
    if col.value[0]:
        match col.value[1]:
            case 'left' if direction[0] > 0:
                direction[0] = 0
            case 'right' if direction[0] < 0:
                direction[0] = 0
            case 'top' if direction[1] > 0:
                direction[1] = 0
            case 'bottom' if direction[1] < 0:
                direction[1] = 0


def physics_process():
    move_and_collide()

    player.mesh.x += direction[0]
    player.mesh.y += direction[1]
    player.col_box.x0 += direction[0]
    player.col_box.y0 += direction[1]

    cam_follow_l = player.mesh.x <= 1 + camera.x and direction[0] < 0
    cam_follow_r = player.mesh.x >= 12 + camera.x and direction[0] > 0
    cam_follow_u = player.mesh.y <= 1 + camera.y and direction[1] < 0
    cam_follow_d = player.mesh.y >= 6 + camera.y and direction[1] > 0

    if cam_follow_l or cam_follow_r:
        camera.x += direction[0]
    if cam_follow_u or cam_follow_d:
        camera.y += direction[1]
   
    p_col = player.col_box
    o_col = obstacle.col_box
    
    col.value = detect_col(player.col_box, obstacle.col_box)
    

    direction[0] = 0
    direction[1] = 0

def input_process(action):
    if action == 'dtw':
        game_state.is_running = False

    match action:
        case 'a':
            direction[0]=(-1)
        case 'd':
            direction[0]=1
        case 'w':
            direction[1]=(-1)
        case 's':
            direction[1]=1
