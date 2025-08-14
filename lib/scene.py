_scene = {}

def add_obj(name, obj):
    _scene[name] = obj

def get_obj(name):
    return _scene[name]

def get_scene():
    return _scene.copy()

