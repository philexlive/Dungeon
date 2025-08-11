class ColBox():
    def __init__(self, x0, y0, x1, y1):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1

def col_direction(col_box0, col_box1):
    t_col = col_box0.y0 + col_box0.y1 - col_box1.y0
    b_col = col_box1.y0 + col_box1.y1 - col_box0.y0
    l_col = col_box0.x0 + col_box0.x1 - col_box1.x0
    r_col = col_box1.x0 + col_box1.x1 - col_box0.x0
    
    if t_col < b_col and t_col < l_col and t_col < r_col:
        return 'top'
    if b_col < t_col and b_col < l_col and b_col < r_col:
        return 'bottom'
    if l_col < r_col and l_col < t_col and l_col < b_col:
        return 'left'
    if r_col < l_col and r_col < t_col and r_col < b_col:
        return 'right'
    return None


def detect_col(col_box0, col_box1):
    direction = col_direction(col_box0, col_box1)

    collision_x = col_box0.x0 + col_box0.x1 >= col_box1.x0 and col_box1.x0 + col_box1.x1 >= col_box0.x0

    collision_y = col_box0.y0 + col_box0.y1 >= col_box1.y0 and col_box1.y0 + col_box1.y1 >= col_box0.y0

    if collision_x and collision_y:
        return (collision_x and collision_y, direction)
    
    return (False, 'no_col')

