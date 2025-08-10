from lib.render import draw


class Obj:
    def __init__(self, pos, mesh):
        self.x, self.y = pos
        self.mesh = mesh

obj1 = Obj(
    (2, 2),
    [
        ['*', '.', '.', '*'],
        ['.', '.', '*', '.'],
        ['.', '*', '.', '.'],
        ['*', '.', '.', '*'],
    ]
)


def obj_to_primitives(obj):
    primitives = []
    x_len, y_len = (len(obj.mesh), len(obj.mesh[0])) if obj.mesh else (0, 0)
    for y in range(y_len):
        for x in range(x_len):
            
            primitives.append((x+obj.x, y+obj.y, obj.mesh[y][x]))
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
