from lib.physics import ColBox
from lib.viewport import Mesh
from lib.gameobj import PhyObj

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
    'mask': 'int'
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
                v = _convert_val(i, value('='), phyobj_rule)
                tokens[group][i] = v
    phyobj = PhyObj(
        **tokens['self'],
        mesh=Mesh(**tokens['mesh']),
        col_box=ColBox(**tokens['colbox'])
    )
    return phyobj
            

def _convert_val(i, v, rule):
    match rule[i]:
        case 'int':
            return int(v)
        case 'bool':
            return bool(v)
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

