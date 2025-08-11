from lib.render import draw


class Mesh:
    def __init__(self, pos, tex):
        self.x, self.y = pos
        self.tex = tex


def obj_to_primitives(obj):
    primitives = []
    x_len, y_len = (len(obj.tex), len(obj.tex[0])) if obj.tex[0] else (0, 0)
    for y in range(y_len):
        for x in range(x_len):
            
            primitives.append((x+obj.x, y+obj.y, obj.tex[y][x]))
    return primitives



def draw_viewport(pos, size, *objs):
    primitives = []

    for obj in objs:
        primitives += obj_to_primitives(obj)

    draw_within(pos[0], pos[1], size[0], size[1], *primitives)
        


def draw_within(x0, y0, x1, y1, *args):
    for arg in args:
        x_within = arg[0] in range(x0, x1)
        y_within = arg[1] in range(y0, y1)

        if x_within and y_within:
            draw(arg[0], arg[1], arg[2])
