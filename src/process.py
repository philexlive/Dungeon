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
    col_box=ColBox(
        2, 2, 1, 1,
        layer=1,
        mask=2
    ),
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
    col_box=ColBox(
        3, 3, 4, 4,
        layer=2,
        mask=-1
    ),
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
    col_box=ColBox(
        6, 6, 4, 4,
        layer=2,
        mask=-1
    ),
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

objs = [
    player,
    obstacle,
    obstacle1,
]

def draw_process():
    draw_frame()
    draw_hp_bar((18, 1), 3)
    draw_inventory((18, 3), *['->==>', '[DDD]', 'o--++', None])
    draw_actions((0, 9), "{'a'-left, 's'-down, 'w'-up, 'd'-right, 'dtw'-destroy this world}")
    meshes = map(lambda obj: obj.mesh, objs)
    draw_viewport((1, 1), (13, 7), camera, *meshes)
    log(1, x=player.mesh.x, y=player.mesh.y, collides=col.value)


direction = [0, 0]
velocity = {'x':0, 'y':0}

def move_and_collide(obj, velocity):
    col_boxes = map(lambda o: o.col_box, objs)
    objs_to_check = [o for o in col_boxes if o.layer == obj.col_box.mask and o != obj.col_box]

    for o in objs_to_check:
        direction = detect_col(obj.col_box, o)[1]
        
        match direction:
            case 'left' if velocity['x'] > 0:
                velocity['x'] = 0
            case 'right' if velocity['x'] < 0:
                velocity['x'] = 0
            case 'top' if velocity['y'] > 0:
                velocity['y'] = 0
            case 'bottom' if velocity['y'] < 0:
                velocity['y'] = 0

    player.mesh.x += velocity['x']
    player.mesh.y += velocity['y']
    player.col_box.x0 += velocity['x']
    player.col_box.y0 += velocity['y']


def physics_process():
    cam_follow_l = player.mesh.x <= 2 + camera.x and velocity['x'] < 0
    cam_follow_r = player.mesh.x >= 11 + camera.x and velocity['x'] > 0
    cam_follow_u = player.mesh.y <= 2 + camera.y and velocity['y'] < 0
    cam_follow_d = player.mesh.y >= 5 + camera.y and velocity['y'] > 0

    if cam_follow_l or cam_follow_r:
        camera.x += velocity['x']
    if cam_follow_u or cam_follow_d:
        camera.y += velocity['y']
   
    p_col = player.col_box
    o_col = obstacle.col_box
    
    cols = map(lambda obj: obj.col_box, objs)
    for i in cols:
        for j in cols:
            col.value = detect_col(i, j)
            break 

    # Player collisions
    move_and_collide(player, velocity)
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
