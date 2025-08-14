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
from lib.gameobj import PhyObj
from lib.ui import draw_frame
from lib.ui import draw_hp_bar
from lib.ui import draw_inventory
from lib.ui import draw_actions
from lifecycle import game_state


def init_game():
    change_prompt('Y->==> ')

    player = PhyObj(
        mesh=Mesh((2, 2), [['Y']]),
        col_box=ColBox(
            2, 2, 1, 1,
            layer=1,
            mask=2
        ),
    )
    obstacles = [
        PhyObj(
            mesh=Mesh(
                (3, 3),
                [
                    ['*', '.', '.', '*'],
                    ['.', '.', '*', '.'],
                    ['.', '*', '.', '.'],
                    ['*', '.', '.', '*'],
                ]
            ),
            col_box=ColBox(
                3, 3, 4, 4,
                layer=2,
                mask=-1
            ),
        ),
        PhyObj(
            mesh=Mesh(
                (6, 6),
                [
                    ['*', '.', '.', '*'],
                    ['.', '.', '*', '.'],
                    ['.', '*', '.', '.'],
                    ['*', '.', '.', '*'],
                ]
            ),
            col_box=ColBox(
                6, 6, 4, 4,
                layer=2,
                mask=-1
            ),
        )
    ]

    add_obj('player', player)
    for i in range(len(obstacles)):
        add_obj(f'obstacle{i}', obstacles[i])


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
    draw_actions((0, 9), "{'a'-left, 's'-down, 'w'-up, 'd'-right, 'dtw'-destroy this world}")
    meshes = map(lambda obj: obj.mesh, get_scene().values())
    draw_viewport((1, 1), (13, 7), camera, *meshes)
    log(1, x=get_obj('player').mesh.x, y=get_obj('player').mesh.y)


direction = [0, 0]
velocity = {'x':0, 'y':0}

def physics_process():
    player = get_obj('player')
    move_and_collide(player, velocity)
    
    cam_follow_l = player.mesh.x < 2 + camera.x and velocity['x'] < 0
    cam_follow_r = player.mesh.x > 11 + camera.x and velocity['x'] > 0
    cam_follow_u = player.mesh.y < 2 + camera.y and velocity['y'] < 0
    cam_follow_d = player.mesh.y > 5 + camera.y and velocity['y'] > 0

    if cam_follow_l or cam_follow_r:
        camera.x += velocity['x']
    if cam_follow_u or cam_follow_d:
        camera.y += velocity['y']

    velocity['x']=0
    velocity['y']=0


def input_process(action):
    if action == 'dtw':
        game_state.is_running = False

    match action:
        case 'a':
            velocity['x']=(-1)
        case 'd':
            velocity['x']=1 
        case 'w':
            velocity['y']=(-1)
        case 's':
            velocity['y']=1 
