from wisayoengine.graphics.texture_component import TextureComponent

class ReadTextureException(Exception): pass

class ResourceLoader:
    def __init__(self, project, resources):
        self.project = project
        self.resources = resources

    @staticmethod
    def __parse_texture(file):
        def expect(sym):
            nonlocal c
            ignore_delimiters()
            if accept(sym):
                return
            raise ReadTextureException("Unexpected symbol, your texture data corrupted.")

        def accept(sym):
            nonlocal c
            if c == sym:
                c = file.read(1)
                return True
            return False

        def ignore_delimiters():
            nonlocal c
            while c in delimiters:
                c = file.read(1)

        def get_number():
            ignore_delimiters()
            nonlocal c
            nonlocal buffer
            if c in numbers:
                while c in numbers:
                    buffer += c
                    c = file.read(1)

        delimiters = [' ', '\n', '\n']
        numbers = [f"{i}" for i in range(10)]

        buffer = ''

        c = file.read(1)

        expect('[')

        get_number()
        width = buffer
        buffer = ''

        expect(',')

        get_number()
        height = buffer
        buffer = ''

        expect(']')
        expect('$')

        while c != '':
            ignore_delimiters()
            buffer += c
            c = file.read(1)

        return TextureComponent(buffer, int(width), int(height))

    def load_texture(self, file_name):
        with open(f"{self.project}/{self.resources}/{file_name}") as file:
            return self.__parse_texture(file)
