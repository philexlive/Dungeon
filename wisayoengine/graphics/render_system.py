from .texture_component import TextureComponent


class RenderSystem:
    def __init__(self, renderer, width, height, component_manager):
        self.width = width
        self.height = height
        self.renderer = renderer
        self.component_manager = component_manager

    def append_element(self, element):
        x_s = element[1].x + element[0].width
        y_s = element[1].y + element[0].height

        is_within_width = x_s > 0 and element[1].x < self.width
        is_within_height = y_s > 0 and element[1].y < self.height

        if is_within_width or is_within_height:
            self.elements.append(element)

    def render(self):
        for element in self.component_manager.fetch_with(TextureComponent):
            self.append_element(element)

        for element in self.elements:
            self.prepare_texture(element[0], element[1])

    def prepare_texture(self, texture, position):
        column = 0
        row = 0
        for c in list(texture.data):
            if c == '/':
                row += 1
                column = 0
                continue

            self.renderer.draw(column + position.x, row + position.y, c)
            column += 1
