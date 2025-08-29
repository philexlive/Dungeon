import time

from .graphics.render_system import RenderSystem
from .io.input_system import InputSystem


class Engine:
    def __init__(self, renderer, input_handler, component_manager):
        self.input_system = InputSystem(input_handler)

        self._renderer = renderer
        self._render_system = RenderSystem(renderer, 50, 12, component_manager)

    def run(self):
        while True:
            # Input
            self.input_system.handle_input()

            # Rendering
            self._renderer.clear()

            self._render_system.render()

            self._renderer.show()

            time.sleep(1.0/12)


