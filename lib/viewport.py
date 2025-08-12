from lib.render import draw


class Mesh:
    def __init__(self, pos, tex):
        self.x, self.y = pos
        self.tex = tex


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



def draw_viewport(pos, size, *objs):
    """Draw bounded viewport.

    :param pos: tuple - position of the viewport by x and y.
    :param size: tuple - size of the viewport, witdh and height.
    :param *objs: mesh - objects to draw into viewport

    Function to draw multiple objects within bounded viewport 
    on the sceen.
    """
    
    primitives = []

    # Gets primitives
    for obj in objs:
        primitives += obj_to_primitives(obj)

    # Draws within the bounded space
    draw_within(pos[0], pos[1], size[0], size[1], *primitives)
        


def draw_within(x0, y0, x1, y1, *args):
    """Draws within a bounded space into the screen.
    
    :param x0: int - left bound of the space.
    :param y0: int - top bound of the space.
    :param x1: int - right bound of the space.
    :param y1: int - bottom bound of the space.
    :param *args: tuple - primitives to draw.

    Function to draw all got primitives within 
    x0, y0, x1, y1 boundaries.
    """
    
    for arg in args:
        x_within = arg[0] in range(x0, x1)
        y_within = arg[1] in range(y0, y1)

        if x_within and y_within:
            draw(arg[0], arg[1], arg[2])
