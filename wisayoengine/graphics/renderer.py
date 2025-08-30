class Renderer:
    def __init__(self):
        self.buffer = []

    def draw(self, x, y, p):
        raise NotImplemented

    def clear(self):
        raise NotImplemented

    def show(self):
        raise NotImplemented