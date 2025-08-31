from wisayoengine.core.vector import Vector


class Entity:
    def __init__(self, identity):
        self.identity = identity

class Lexeme:
    def __init__(self):
        self.name = Lexeme.__name__
        self.position = Vector(0, 0)
