from common.entity import Entity


class ComponentManager:
    def __init__(self):
        self.entities = []
        self.entity_ids = {}

        self.positions = []
        self.position_ids = {}

        self.textures = []
        self.texture_ids = {}

        self.cameras = []
        self.cameras_ids = []

    def fetch_with(self, component):
        return [(self.textures[0], self.positions[0])]


    def append(self, __object):
        if not any(isinstance(component, Entity) for component in __object):
            raise Exception("This is not an entity.")
        self.textures.append(__object[1])
        self.positions.append(__object[2])