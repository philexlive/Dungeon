_width = 50
_height = 12


_screen = [[' ' for row in range(_width)] for column in range(_height)]


def draw(x, y, c):
    if x >= _width or y >= _height:
        return
    
    if x <= -_width or y <= -_height:
        return

    _screen[y][x] = c



def _draw_line_low(x0, y0, x1, y1, c, /):
    dx = x1 - x0 
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0 

    for x in range(x0, x1):
        draw(x, y, c)
        if D > 0:
            y = y + yi 
            D = D + 2*(dy - dx)
        else:
            D = D + 2*dy


def _draw_line_high(x0, y0, x1, y1, c, /):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0 

    for y in range(y0, y1):
        draw(x, y, c)
        if D > 0:
            x = x + xi
            D = D + 2*(dx - dy)
        else:
            D = D + 2*dx


def draw_line(start, end, c):
    x0, y0 = start
    x1, y1 = end

    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            _draw_line_low(x1, y1, x0, y0, c)
        else:
            _draw_line_low(x0, y0, x1, y1, c)
    else:
        if y0 > y1:
            _draw_line_high(x1, y1, x0, y0, c)
        else:
            _draw_line_high(x0, y0, x1, y1, c)
            

def render():
    for row in _screen:
        for column in row:
            print(column, end='')
        print()

    for row in range(_height):
        for column in range(_width):
            _screen[row][column] = ' '
