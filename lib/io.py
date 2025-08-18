from lib.physics import ColBox
from lib.physics import Velocity
from lib.viewport import Mesh
from lib.phyobj import PhyObj


phyobj_rule = {
    'pos_x': 'int',
    'pos_y': 'int',
    'x': 'int',
    'y': 'int',
    'tex': 'texture',
    'x0': 'int',
    'y0': 'int',
    'x1': 'int',
    'y1': 'int',
    'enabled': 'bool',
    'layer': 'int',
    'mask': 'int',
    'inherit': 'bool'
}


def parse_phyobj(directory, file):
    tokens = {}
    path = directory + file
    with open(path, 'r') as f:
        for line in f:
            ln = line.strip()
            value = lambda c: ln[ln.index(c)+1:]
            identifier = lambda c: ln[:ln.index(c)]
            if '@' in ln:
                group = value('@')
                tokens[group] = {}
            elif '=' in ln:
                i = identifier('=')
                v = convert_val(i, value('='), phyobj_rule)
                tokens[group][i] = v
                
    mesh = None
    colbox = None
    velocity = Velocity(0, 0)

    if tokens['mesh']:
        mesh = Mesh(**tokens['mesh'])
    if tokens['colbox']:
        colbox = ColBox(**tokens['colbox'])
    if tokens['velocity']:
        velocity = Velocity(**tokens['velocity'])

    phyobj = PhyObj(
        **tokens['self'],
        mesh=mesh,
        colbox=colbox,
        velocity = velocity
    )
    return phyobj


def convert_val(i, v, rule):
    match rule[i]:
        case 'int':
            return int(v)
        case 'bool':
            if v.lower() == 'true':
                return True
            else:
                return False
        case 'texture':
            return read_tex(v)
        case _:
            return v


def read_tex(path):
    tex = []
    with open(path, 'r') as f:
        for line in f:
            ln = line.strip()
            tex.append(list(ln))
    return tex

