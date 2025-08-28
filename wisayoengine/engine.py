import time

from graphics.renderer import Renderer
from graphics.render_system import RenderSystem
from common.entity import Entity
from common.vec import Vec
from component_manager import ComponentManager
from resource_loader import ResourceLoader


class Engine:
    def __init__(self, renderer):
        self.component_manager = ComponentManager()

        self._renderer = renderer
        self._render_system = RenderSystem(renderer, 50, 12, self.component_manager)

    def run(self):
        while True:

            # Rendering
            self._renderer.clear()

            self._render_system.render()

            self._renderer.show()

            time.sleep(1.0/12)


import os

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
        (Entity('1'), resource_loader.load_texture('box.texture'), Vec(3, 1))
    )

    engine.run()