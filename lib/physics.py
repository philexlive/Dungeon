from lib.scene import get_scene

# TODO: remove duplicates

class ColBox():
    def __init__(self, x0, y0, x1, y1, enabled=True, layer=0, mask=0):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.enabled = enabled
        self.layer = 0
        self.mask = 0

def _col_direction(col_box0, col_box1, pos0, pos1):
    pos_x0, pos_y0 = pos0
    pos_x1, pos_y1 = pos1
    
    pos_x_rel0 = col_box0.x0 + pos_x0
    pos_y_rel0 = col_box0.y0 + pos_y0
    pos_x_rel1 = col_box1.x0 + pos_x1
    pos_y_rel1 = col_box1.y0 + pos_y1
    
    t_col = pos_y_rel0 + col_box0.y1 - pos_y_rel1
    b_col = pos_y_rel1 + col_box1.y1 - pos_y_rel0
    l_col = pos_x_rel0 + col_box0.x1 - pos_x_rel1
    r_col = pos_x_rel1 + col_box1.x1 - pos_x_rel0
    
    if t_col < b_col and t_col < l_col and t_col < r_col:
        return 'top'
    if b_col < t_col and b_col < l_col and b_col < r_col:
        return 'bottom'
    if l_col < r_col and l_col < t_col and l_col < b_col:
        return 'left'
    if r_col < l_col and r_col < t_col and r_col < b_col:
        return 'right'
    return None


def detect_col(col_box0, col_box1, pos0, pos1):
    """Detect collision of two collision boxes.
    :param col_box0: ColBox - First collision box.
    :param col_box1: ColBox - Second collision box.

    :returns: tuple - (bool, str), where bool tells it collides or not,
                      and the str is a direction where the col_box1 was
                      hit by the col_box0.

    Function for detection a collision and its direction 
    of two collision boxes.
    """

    pos_x0, pos_y0 = pos0
    pos_x1, pos_y1 = pos1
    
    pos_x_rel0 = col_box0.x0 + pos_x0
    pos_y_rel0 = col_box0.y0 + pos_y0
    pos_x_rel1 = col_box1.x0 + pos_x1
    pos_y_rel1 = col_box1.y0 + pos_y1
    
    collision_x = pos_x_rel0 + col_box0.x1 >= pos_x_rel1 and pos_x_rel1 + col_box1.x1 >= pos_x_rel0 

    collision_y = pos_y_rel0 + col_box0.y1 >= pos_y_rel1 and pos_y_rel1 + col_box1.y1 >= pos_y_rel0 

    if collision_x and collision_y:
        return _col_direction(col_box0, col_box1, pos0, pos1)
    
    return None 


def move_and_collide(obj, velocity):
    objs = get_scene().values()

    for o in objs:
        direction = detect_col(
                obj.col_box, o.col_box, 
                (obj.pos_x, obj.pos_y), (o.pos_x, o.pos_y)
                )
        match direction:
            case 'left' if velocity['x'] > 0:
                velocity['x'] = 0
            case 'right' if velocity['x'] < 0:
                velocity['x'] = 0
            case 'top' if velocity['y'] > 0:
                velocity['y'] = 0
            case 'bottom' if velocity['y'] < 0:
                velocity['y'] = 0

    obj.pos_x += velocity['x']
    obj.pos_y += velocity['y']
    
