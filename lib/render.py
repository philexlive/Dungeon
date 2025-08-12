_width = 50
_height = 12


_screen = [[' ' for row in range(_width)] for column in range(_height)]


def draw(x, y, c, /):
    """Draw one character on the screen.

    :param x: int - Position of the pixel by x axis.
    :param y: int - Position of the pixel by y axis.
    :param c: str - Character to draw.

    Function to draw one character on the screen at x an y posisition.
    """

    # Check if the x and y inside the screen
    if x >= _width or y >= _height or x < 0 or y < 0:
        return

    # Inserts the character into the screen
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
    """Draw a line on the screen.

    :param start: tuple - starting point position by x and y.
    :param end: tuple - end point position by x and y.
    :param c: str - character representing one single unit of the line.

    Function to draw one line from starting to end point on the screen,
    that uses Bresenham's line algorithm
    """
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
    """Renders the screen to the CLI.
    """
    for row in _screen:
        for column in row:
            print(column, end='')
        print()

    for row in range(_height):
        for column in range(_width):
            _screen[row][column] = ' '
