from lib.render import draw


def viewport(position, size, *args):
    x0, y0 = position
    x1, y1 = size
    
    for y in range(y0, y1):
        for x in range(x0, x1):
            draw(x, y, ' ')

    for arg in args:
        is_within_x = arg[0][0] in range(x0, x1)
        is_within_y = arg[0][1] in range(y0, y1)
        if is_within_x and is_within_y:
            draw(arg[0][0], arg[0][1], arg[1])
