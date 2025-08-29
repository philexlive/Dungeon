import random

from wisayoengine.core import Position
from wisayoengine.core.entity import Entity
from wisayoengine.graphics.camera import Camera
from wisayoengine.graphics.texture import Texture


class FindObjectError(Exception): pass


class ComponentManager:
    def __init__(self):
        self.entities = []
        self.entities_relation = []

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

    def get_indices(self):
        return list(map(lambda entity: entity.identity, self.entities))

    def get_with_id(self, identity):
        for entity in self.entities:
            if entity.identity == identity:
                temp = []
                if entity.identity in self.positions:
                    temp.append(self.positions[entity.identity])
                elif entity.identity in self.textures:
                    temp.append(self.textures[entity.identity])
                elif entity.identity in self.cameras:
                    temp.append(self.cameras[entity.identity])

                return temp

        raise FindObjectError

    def get_position(self, identity):
        return self.positions[self.position_ids[identity]]

    def append(self, obj):
        new_entity = Entity(self.get_unique_id())

        for component in obj:
            if isinstance(component, Position):
                l = len(self.positions)
                self.positions.append(component)
                self.position_ids[new_entity.identity] = l
            elif isinstance(component, Texture):
                l = len(self.textures)
                self.textures.append(component)
                self.texture_ids[new_entity.identity] = l
            elif isinstance(component, Camera):
                l = len(self.cameras)
                self.cameras.append(component)
                self.camera_ids[new_entity.identity] = l

        self.entities.append(new_entity)

        print("New entity just added")

    def get_unique_id(self):
        symbols = "abcdefghjklmnopqrstuvwxyz0123456789"
        get_id = lambda:"".join([random.choice(symbols) for _ in range(8)])
        new_id = get_id()
        while new_id in map(lambda entity: entity.identity, self.entities):
            new_id = get_id()

        return new_id