from wisayoengine.graphics.draw_pack import DrawPack
from wisayoengine.graphics.texture import Texture

class ReadTextureException(Exception): pass

class TextureParser:
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
            temp = ''
            while c in numbers:
                temp += c
                c = file.read(1)
            return int(temp)

        delimiters = [' ', '\n', '\t']
        numbers = [f"{i}" for i in range(10)]

        c = file.read(1)

        expect('[')

        width = get_number()

        ignore_delimiters()

        expect(',')

        height = get_number()

        ignore_delimiters()
        expect(']')
        expect('$')

        column = 0
        row = 0
        draw_pack = DrawPack()
        while c != '':
            if accept('\n') or accept(' '):
                continue

            if accept('\\'):
                if accept('s'):
                    draw_pack.append((column, row, ' '))
                elif accept('n'):
                    row += 1
                    column = 0
                elif accept('\\'):
                    draw_pack.append((column, row, c))
                else:
                    raise ReadTextureException(f"Wrong escape character '{c}' at {file.tell(), row}")
            else:
                draw_pack.append((column, row, c))
                c = file.read(1)
            column += 1
        return Texture(draw_pack, int(width), int(height))

    def load_texture(self, path):
        with open(path) as file:
            return self.__parse_texture(file)
