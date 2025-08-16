# TODO: Replace this REALLY VEIRD code

from lib.physics import ColBox
from lib.viewport import Mesh
from lib.gameobj import PhyObj

phy_obj_rule = {
    b'pos_x': 'int',
    b'pos_y': 'int',
    b'mesh': 'Mesh',
    b'col_box': 'ColBox'
}

mesh_rule = {
    b'x': 'int',
    b'y': 'int',
    b'tex': 'list'
}

col_box_rule = {
    b'x0': 'int',
    b'y0': 'int',
    b'x1': 'int',
    b'y1': 'int',
    b'enabled': 'bool',
    b'layer': 'int',
    b'mask': 'int'
}

def build_obj(directory, file):
    obj_t, tokens = get_tree(directory, file)
    match obj_t:
        case 'PhyObj':
            obj = PhyObj(
                    **tokens['self'], 
                    mesh=Mesh(**tokens['mesh']),
                    col_box=ColBox(**tokens['col_box'])
                )
            print(obj.mesh.tex)
            return obj
        case 'Mesh':
            return PhyObj(**tokens['self'])
        case 'ColBox':
            return PhyObj(**tokens['self'])
    return None

def get_tree(directory, file):
    obj_t = b''
    tokens = {}

    group = b''
    path = str(directory) + str(file)
    with open(path, 'rb') as f:
        for ln in f:
            if b'@' in ln:
                sign_i = ln.index(b'@')
                st = ln.strip()
                group = st[sign_i+1:]
                tokens[group.decode()] = {}
            elif b'=' in ln:
                sign_i = ln.index(b'=')
                st = ln.strip()
                v = st[:sign_i]
                if v in [b'mesh', b'col_box', b'tex']:
                    f_name = st[sign_i+1:].decode("ascii")
                    if v == b'tex':
                        tokens[group.decode()][v.decode()] = read_tex(directory, f_name) 
                    else:
                        group = v
                        mesh_tree = get_tree(directory, f_name)[1]
                        tokens[group.decode()] = mesh_tree['self']
                else:
                    rule = {}
                    match group:
                        case b'self' if obj_t == b'Mesh':
                            rule = mesh_rule
                        case b'self' if obj_t == b'ColBox':
                            rule = col_box_rule
                        case b'self' if obj_t == b'PhyObj':
                            rule = phy_obj_rule
                        case b'col_box':
                            rule = col_box_rule
                        case b'mesh':
                            rule = mesh_rule
                        case _:
                            rule = col_box_rule
                    tokens[group.decode()][v.decode()] = _convert_val(rule[v], st[sign_i+1:])
            elif ln != b'\n' and obj_t == b'':
                st = ln.strip()
                obj_t = st
            elif ln != b'\n' and obj_t != b'': 
                raise NameError("Wrong expression '{ln}'")

        return (obj_t.decode(), tokens)

def _convert_val(t, v):
    match t:
        case 'int':
            return int(v)
        case 'bool':
            return bool(v)
        case _:
            return v

def read_tex(directory, file):
    tex = []
    with open(directory + file, 'r') as f:
        i = 0
        for ln in f:
            tex.append([])
            for ch in ln.strip():
                tex[i].append(ch) 

            i += 1
    return tex
