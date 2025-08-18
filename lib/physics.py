from lib.scene import get_scene


class ColBox():
    def __init__(self, x0, y0, x1, y1, enabled, layer, mask):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.enabled = enabled
        self.layer = 0
        self.mask = 0

class Velocity():
    def __init__(self, x, y):
        self.x, self.y = x,  y


def detect_col(colbox0, colbox1, pos0, pos1):
    """Detect collision of two collision boxes.
    :param col_box0: ColBox - First collision box.
    :param col_box1: ColBox - Second collision box.

    :returns: tuple - (bool, str), where bool tells it collides or not,
                      and the str is a direction where the col_box1 was
                      hit by the col_box0.

    Function for detection a collision and its direction 
    of two collision boxes.
    """
    if not colbox0.enabled or not colbox1.enabled:
        print("not enabled")
        return None

    pos_x0, pos_y0 = pos0
    pos_x1, pos_y1 = pos1
    
    pos_x_rel0 = colbox0.x0 + pos_x0
    pos_y_rel0 = colbox0.y0 + pos_y0
    pos_x_rel1 = colbox1.x0 + pos_x1
    pos_y_rel1 = colbox1.y0 + pos_y1
    
    collision_x = pos_x_rel0 + colbox0.x1 >= pos_x_rel1 and pos_x_rel1 + colbox1.x1 >= pos_x_rel0 

    collision_y = pos_y_rel0 + colbox0.y1 >= pos_y_rel1 and pos_y_rel1 + colbox1.y1 >= pos_y_rel0 

    if not collision_x and not collision_y:
        print("no collision")
        return
    
    t_col = pos_y_rel0 + colbox0.y1 - pos_y_rel1
    b_col = pos_y_rel1 + colbox1.y1 - pos_y_rel0
    l_col = pos_x_rel0 + colbox0.x1 - pos_x_rel1
    r_col = pos_x_rel1 + colbox1.x1 - pos_x_rel0
    
    if t_col < b_col and t_col < l_col and t_col < r_col:
        return 'top'
    if b_col < t_col and b_col < l_col and b_col < r_col:
        return 'bottom'
    if l_col < r_col and l_col < t_col and l_col < b_col:
        return 'left'
    if r_col < l_col and r_col < t_col and r_col < b_col:
        return 'right'


def move_and_collide(phyobj):
    """Check object for collisions in scene.
    
    :param phyobj: PhyObj - physical object to check for collisions.
    """
    phyobjs = get_scene().values()

    for o in phyobjs:
        direction = detect_col(
                phyobj.colbox, o.colbox, 
                (phyobj.pos_x, phyobj.pos_y), (o.pos_x, o.pos_y)
                )
        match direction:
            case 'left' if phyobj.velocity.x > 0:
                phyobj.velocity.x = 0
            case 'right' if phyobj.velocity.x < 0:
                phyobj.velocity.x = 0
            case 'top' if phyobj.velocity.y > 0:
                phyobj.velocity.y = 0
            case 'bottom' if phyobj.velocity.y < 0:
                phyobj.velocity.y = 0

    phyobj.pos_x += phyobj.velocity.x
    phyobj.pos_y += phyobj.velocity.y

