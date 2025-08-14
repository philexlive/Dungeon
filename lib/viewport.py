from lib.render import draw


class Mesh:
    def __init__(self, pos, tex):
        self.x, self.y = pos
        self.tex = tex

class Camera:
    def __init__(self, x, y):
        self.x, self.y = x, y


def obj_to_primitives(obj):
    """Convert mesh to its primitives.
    
    :param obj: Mesh - a mesh convert to.

    Function to convert a mesh to a list of primitives,
    which are tuples with position on the 2d plane and 
    a character to draw.
    """
    
    primitives = []
    x_len, y_len = (len(obj.tex), len(obj.tex[0])) if obj.tex[0] else (0, 0)
    for y in range(y_len):
        for x in range(x_len):
            
            primitives.append((x+obj.x, y+obj.y, obj.tex[y][x]))
    return primitives



def draw_viewport(pos, size, camera, *objs):
    """Draw bounded viewport.

    :param pos: tuple - position of the viewport by x and y.
    :param size: tuple - size of the viewport, witdh and height.
    :param camera: Camera - camera object to make 
                            viewport position relative
    :param *objs: mesh - objects to draw into viewport

    Function to draw multiple objects within bounded viewport 
    on the sceen.
    """
    
    primitives = []

    # Gets primitives
    for obj in objs:
        primitives += obj_to_primitives(obj)

    # Draws within the bounded space
    draw_within(
        pos[0], 
        pos[1], 
        size[0], 
        size[1], 
        camera.x, 
        camera.y, 
        *primitives
    )
        


def draw_within(x0, y0, x1, y1, x_rel, y_rel, *args):
    """Draws within a bounded space into the screen.
    
    :param x0: int - left bound of the space.
    :param y0: int - top bound of the space.
    :param x1: int - right bound of the space.
    :param y1: int - bottom bound of the space.
    :param x_rel: int - x value a primitive relative to
    :param y_rel: int - y value a primitive relative to
    :param *args: tuple - primitives to draw.

    Function to draw all primitives relatively within 
    x0, y0, x1, y1 boundaries.
    """
    
    for arg in args:
        x = arg[0] - x_rel
        y = arg[1] - y_rel
        
        x_within = x in range(x0, x1)
        y_within = y in range(y0, y1)
        if x_within and y_within:
            draw(x, y, arg[2])
