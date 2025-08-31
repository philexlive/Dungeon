from wisayoengine.core import Vector
from wisayoengine.core.transform import Transform


class RenderSystem:
    def __init__(self, renderer, width, height, component_manager):
        self.width = width
        self.height = height
        self.renderer = renderer
        self.component_manager = component_manager

    def render(self):
        for element in self.component_manager.fetch_textures():
            x_s = element['position'].x + element['texture'].width
            y_s = element['position'].y + element['texture'].height

            is_within_width = x_s > 0 and element['position'].x < self.width
            is_within_height = y_s > 0 and element['position'].y < self.height

            if is_within_width or is_within_height:
                row = 0
                column = 0
                for p in element['texture'].draw_pack:
                    x = element['position'].x
                    y = element['position'].y
                    translated = Transform().get_translated(Vector(x, y))
                    rotated = Transform().get_rotated(element['rotation'].angle)
                    scaled = rotated.get_scaled(element['scale'])

                    result = translated * rotated * scaled
                    vertex = Vector(
                        result.x_axis.x * (column-2) + result.x_axis.y * (row -2)+ result.origin.x,
                        result.y_axis.x * (column-2) + result.y_axis.y * (row -2) + result.origin.y,
                    )

                    self.renderer.draw(
                        vertex.x + x,
                        vertex.y + y,
                        p
                    )

                    if column < 3:
                        column += 1
                    else:
                        row += 1
                        column = 0

                element['texture'].draw_pack.reset()
