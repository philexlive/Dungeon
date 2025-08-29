class DrawPack:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index - 1]

    def reset(self):
        self.index = 0

    def append(self, item):
        self.data.append(item)