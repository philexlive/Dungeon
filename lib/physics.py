from lib.scene import get_scene


class ColBox():
    def __init__(self, 
                 x0=0, 
                 y0=0,
                 x1=1, 
                 y1=1, 
                 enabled=True, 
                 layer=1,
                 mask=1
                 ):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.enabled = enabled
        self.layer = layer
        self.mask = mask


class Velocity():
    def __init__(self, x=0, y=0):
        self.x, self.y = x,  y


def detect_col(colbox0, colbox1, pos0, pos1):
    """Detect collision of two collision boxes.

    :param colbox0: ColBox - First collision box.
    :param colbox1: ColBox - Second collision box.
    :param pos0: int - position of colbox0 relative to.
    :param pos1: int - position of colbox1 relative to.

    :returns: str - Is a direction where the col_box1 was
                    hit by the col_box0.

    Function for detection a collision and its direction 
    of two collision boxes.
    """
    
    colboxes_exist = colbox0 and colbox1
    if not colboxes_exist:
        return None

    enabled = colbox0.enabled and colbox1.enabled
    if not enabled:
        return None

    pos_x0, pos_y0 = pos0
    pos_x1, pos_y1 = pos1
    
    pos_x_rel0 = colbox0.x0 + pos_x0
    pos_y_rel0 = colbox0.y0 + pos_y0
    pos_x_rel1 = colbox1.x0 + pos_x1
    pos_y_rel1 = colbox1.y0 + pos_y1

    collision_x = pos_x_rel0 + colbox0.x1 >= pos_x_rel1 and pos_x_rel1 + colbox1.x1 >= pos_x_rel0 

    collision_y = pos_y_rel0 + colbox0.y1 >= pos_y_rel1 and pos_y_rel1 + colbox1.y1 >= pos_y_rel0 

    collides = collision_x and collision_y
    if not collides:
        return None

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
    """Check object for collisions in scene and move.
    
    :param phyobj: PhyObj - physical object to check for collisions.

    Check one object for collisions with others in current scene 
    to move properly.
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

