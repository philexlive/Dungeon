import random
from .entity import Entity
from .position_component import PositionComponent
from wisayoengine.graphics.camera import CameraComponent
from wisayoengine.graphics.texture_component import TextureComponent


class ComponentManager:
    def __init__(self):
        self.entities = []

        self.positions = []
        self.position_ids = {}

        self.textures = []
        self.texture_ids = {}

        self.cameras = []
        self.camera_ids = {}

    def fetch_textures(self):
        get_texture = lambda k: self.textures[self.texture_ids[k]]
        get_position = lambda k: self.positions[self.position_ids[k]]
        return [
            {'texture': get_texture(k), 'position': get_position(k)}
            for k in self.texture_ids
        ]

    def append(self, obj):
        new_entity = Entity(self.get_unique_id())

        for component in obj:
            if isinstance(component, PositionComponent):
                l = len(self.positions)
                self.positions.append(component)
                self.position_ids[new_entity.identity] = l
            elif isinstance(component, TextureComponent):
                l = len(self.textures)
                self.textures.append(component)
                self.texture_ids[new_entity.identity] = l
            elif isinstance(component, CameraComponent):
                l = len(self.cameras)
                self.cameras.append(component)
                self.camera_ids[new_entity.identity] = l
            print("appended")

        self.entities.append(new_entity)

        print("New entity just added")

    def get_unique_id(self):
        symbols = "abcdefghjklmnopqrstuvwxyz0123456789"
        get_id = lambda:"".join([random.choice(symbols) for _ in range(8)])
        new_id = get_id()
        while new_id in map(lambda entity: entity.identity, self.entities):
            new_id = get_id()

        return new_id