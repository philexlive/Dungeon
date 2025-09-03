import random

from wisayoengine.core import Vector
from wisayoengine.core.basic_components import Position, Scale
from wisayoengine.core.entity import Entity
from wisayoengine.core.rotation import Rotation
from wisayoengine.core.transform import Transform
from wisayoengine.graphics.camera import Camera
from wisayoengine.graphics.texture import Texture


class FindObjectError(Exception): pass
class IdentityUniquenessError(Exception): pass


class EntityError(Exception): pass


class ComponentManager:
    """Experimental component manager"""

    def __init__(self):
        self.entities = []
        self.entities_relation = []

        self.positions = []
        self.position_ids = {}

        self.scales = []
        self.scale_ids = {}

        self.rotations = []
        self.rotation_ids = {}

        self.transforms = []
        self.transform_ids = {}

        self.textures = []
        self.texture_ids = {}

        self.cameras = []
        self.camera_ids = {}


    def fetch_textures(self):
        get_texture = lambda k: self.textures[self.texture_ids[k]]
        get_position = lambda k: self.positions[self.position_ids[k]]
        get_scale = lambda k: self.scales[self.scale_ids[k]]
        get_rotation = lambda k: self.rotations[self.rotation_ids[k]]
        return [
            {
                'texture': get_texture(k),
                'position': get_position(k),
                'scale': get_scale(k),
                'rotation': get_rotation(k)
            }
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

    def get_rotation(self, identity):
        return self.rotations[self.rotation_ids[identity]]

    def get_scale(self, identity):
        return self.scales[self.scale_ids[identity]]


    def add_entity(self, obj):
        #
        # def check_name(i=0):
        #     nonlocal new_entity
        #     if new_entity.identity in map(lambda entity: entity.identity, self.entities):
        #         new_entity.identity = f"{new_entity.identity}{i}"
        #         check_name(i)

        new_entity: Entity
        for component in obj:
            if isinstance(component, Entity):
                new_entity = component
                obj.remove(new_entity)
                break
        else: new_entity = Entity("entity")
        # check_name()

        for component in obj:
            self.expand_entity(component, new_entity)

        self.entities.append(new_entity)

        return new_entity


    def expand_entity(self, component, entity):
        """Experimental append new object function.

        Gets iterable of components, returns `identity`.
        """
        print(component)
        # Helping function for inserting entity
        def insert(comp_entry, comp_map):
            self.add_comp(comp_entry, comp_map, component, entity)

        if isinstance(component, Transform):
            insert(self.transforms, self.transform_ids)
        elif isinstance(component, Position):
            insert(self.positions, self.position_ids)
        elif isinstance(component, Scale):
            insert(self.scales, self.scale_ids)
        elif isinstance(component, Rotation):
            insert(self.rotations, self.rotation_ids)
        elif isinstance(component, Texture):
            insert(self.textures, self.texture_ids)
        elif isinstance(component, Camera):
            insert(self.cameras, self.camera_ids)


    @staticmethod
    def add_comp(comp_entry, comp_map, component, entity):
        l = len(comp_entry)
        comp_entry.append(component)
        comp_map[entity.identity] = l


component_manager = ComponentManager()


def gen_go():
    return component_manager.add_entity([Entity])


def gen_go2d():
    go2d = [Entity('go2d'),
            Transform(),
            Position(0, 0),
            Scale(0, 0),
            Rotation(0)]
    return component_manager.add_entity(go2d)

def expand_go(component, entity):
    component_manager.expand_entity(component, entity)