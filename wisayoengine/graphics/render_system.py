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
                for i in element['texture'].draw_pack:
                    self.renderer.draw(i[0] + element['position'].x, i[1] + element['position'].y, i[2])
                element['texture'].draw_pack.reset()
