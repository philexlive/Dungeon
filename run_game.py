import os

from wisayoengine.core.position_component import PositionComponent
from wisayoengine.engine import Engine
from wisayoengine.graphics.renderer import Renderer
from wisayoengine.io.resource_loader import ResourceLoader

if __name__ == "__main__":
    class CustomRendererImpl(Renderer):
        def draw(self, x, y, c):
            self._buffer.append((x, y, c))

        def show(self):
            screen = [[' ' for width in range(50)] for height in range(12)]
            for element in self._buffer:
                x = element[0]
                y = element[1]
                if 0 <= x < 50 and 0 <= y < 12:
                    screen[y][x] = element[2]


            for row in screen:
                print(''.join(row))

        def clear(self):
            self._buffer.clear()
            os.system("cls" if os.name == "nm" else "clear")

    render_impl = CustomRendererImpl()
    resource_loader = ResourceLoader('tests', 'res')
    engine = Engine(render_impl)
    engine.component_manager.append(
        [
            resource_loader.load_texture('box.texture'),
            PositionComponent(-1, 10)
        ]
    )

    engine.run()