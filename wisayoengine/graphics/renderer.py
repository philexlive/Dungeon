class Renderer:
    def __init__(self):
        self._buffer = []

    def draw(self, x, y, c):
        raise NotImplemented

    def clear(self):
        raise NotImplemented

    def show(self):
        raise NotImplemented