from src.render import draw_line
from src.render import draw


def draw_frame():
    draw_line((0, 1), (0, 7), '|')
    draw_line((1, 0), (13, 0), '-')
    draw_line((13, 1), (13, 7), '|')
    draw_line((1, 7), (13, 7), '_')

def draw_hp_bar(pos, rate):
    if rate > 4:
        rate = 4

    points = ['-' for i in range(4-rate)] + ['I' for i in range(rate)]
    
    bar = '[ {} ]'.format(' '.join(points))
    
    x, y = pos
    for i in bar:
        draw(x, y, i)
        x += 1


def draw_inventory(pos, /, item1, item2, item3, item4):
    x, y  = pos
    

    for item in [item1, item2, item3, item4]:
        bar = '[ {} ]'.format(item)
        
        if item == None:
            bar = '[       ]'
            
        x_local = x
        for i in bar:
            draw(x_local, y, i)
            x_local += 1
        y += 1


def draw_actions(pos, actions):
    x, y = pos
    for i in actions:
        draw(x, y, i)
        x += 1
