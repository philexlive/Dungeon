from lib.physics import ColBox
from lib.physics import Velocity
from lib.viewport import Mesh
from lib.phyobj import PhyObj


# Rule for phyobj
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
    """Simple parser for .phyobj
    
    :param directory: string - directory file is in.
    :param file: string - a name of file.
    :returns: PhyObj

    Gets file from path (directory+file) to parse them
    to a new PhyObj.
    
    File sample:
    ```player.phyobj
    @self
    pos_x=2
    pos_y=2

    @mesh
    x=-1
    x=-1
    tex=path/to/texture
    
    @colbox
    
    @velocity
    ```

    In the sample code the '@self' represents a group 
    of values will directly put to a final PhyObj, 
    as yo can see, this group doesn't have a value inherit.
    Because most properties has their default value.
    The same thing with groups, if they are empty, the 
    default will be applied.
    """

    tokens = {}
    path = directory + file
    with open(path, 'r') as f:
        for line in f:
            ln = line.strip()

            # Get value from a line using an operator
            value = lambda op: ln[ln.index(op)+1:]
            
            # Get identifier from a line using an operator
            identifier = lambda op: ln[:ln.index(op)]
            
            # Check what operator is on the line
            if '@' in ln:
                # Add a new group to the tokens
                group = value('@')
                tokens[group] = {}
            elif '=' in ln:
                # Get identifier
                i = identifier('=')

                # Get value
                v = convert_val(i, value('='), phyobj_rule)
                
                # Add them to current group
                tokens[group][i] = v

    mesh = None
    colbox = None
    velocity = Velocity(0, 0)


    # Check groups nullability
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
    """Convert value from string to defined by rule.
    :param i: str - statement's identifier.
    :param v: str - statment's literal.
    :param rule: dict - identifier-type rule for converting.

    Gets 'i' as an identifier from a statement and 'v'
    as value to be converted, identifier matches with existing
    on in the 'rule' and got the type the value will be
    converted.
    """

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
    """Reads texture file with any extension.
    
    :param path: str - path to the texture source.
    :returns: list - texuture converted to a 
                     2D list representation.
    """

    tex = []
    with open(path, 'r') as f:
        for line in f:
            ln = line.strip()
            tex.append(list(ln))
    return tex

