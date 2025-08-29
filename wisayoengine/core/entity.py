from wisayoengine.core.position import Position


class Entity:
    def __init__(self, identity):
        self.identity = identity

class Lexeme:
    def __init__(self):
        self.name = Lexeme.__name__
        self.position = Position(0, 0)
