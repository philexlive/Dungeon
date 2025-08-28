import time
from .graphics.render_system import RenderSystem
from .core.component_manager import ComponentManager


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


