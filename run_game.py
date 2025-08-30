import os
from pynput import keyboard
from wisayoengine.core.component_manager import ComponentManager
from wisayoengine.core.position import Position
from wisayoengine.engine import Engine
from wisayoengine.graphics.draw_pack import DrawPack
from wisayoengine.graphics.renderer import Renderer
from wisayoengine.graphics.texture import Texture
from wisayoengine.io.input_api import InputApi


def on_press(key):
    try:
        pressed_keys.add(key.char)
    except AttributeError:
        # Handle special keys
        pressed_keys.add(key)

def on_release(key):
    try:
        if key.char in pressed_keys:
            pressed_keys.remove(key.char)
    except AttributeError:
        if key in pressed_keys:
            pressed_keys.remove(key)

def start_listener():
    """Starts the non-blocking keyboard listener thread."""
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

start_listener()


pressed_keys = set()

if __name__ == "__main__":
    ascii_map = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

    # ________renderer________
    class CustomRendererImpl(Renderer):
        def draw(self, x, y, c):
            self.buffer.append((x, y, c))

        def show(self):
            screen = [[' ' for _ in range(50)] for _ in range(12)]

            for element in self.buffer:
                x = element[0]
                y = element[1]
                if 0 <= x < 50 and 0 <= y < 12:
                    screen[y][x] = ascii_map[int((element[2][3] / 255) * len(ascii_map) - 1) ]

            for row in screen:
                print(''.join(row))

        def clear(self):
            self.buffer.clear()
            os.system("cls" if os.name == "nm" else "clear")
            pass


    # ________component_manager________
    component_manager = ComponentManager()

    draw_pack = DrawPack([
        #  R    G    B    A
        (255,   0,   0,  25),
        (255,   0,   0, 100),
        (  0, 255,   0, 100),
        (  0, 255,   0,  25),

        (255,   0,   0, 100),
        (  0, 255,   0, 255),
        (  0, 255,   0, 255),
        (  0, 255,   0, 100),

        (  0, 255,   0, 100),
        (  0, 255,   0, 255),
        (  0, 255,   0, 255),
        (  0,   0, 255, 100),

        (  0, 255,   0,  25),
        (  0, 255,   0, 100),
        (  0,   0, 255, 100),
        (  0,   0, 255,  25),
    ])
    texture = Texture(draw_pack, 4, 4)

    component_manager.append(
        [texture, Position(0, 0)]
    )
    component_manager.append(
        [texture, Position(4, 4)]
    )

    # ________input________
    class InputApiImpl(InputApi):
        def __init__(self):
            self.cm = component_manager

        def on_input(self):

            direction = (0, 0)

            if 'd' in pressed_keys:
                direction = (1, 0)
            elif 'a' in pressed_keys:
                direction = (-1, 0)
            elif 'w' in pressed_keys:
                direction = (0, -1)
            elif 's' in pressed_keys:
                direction = (0, 1)
                print('s')

            pos = self.cm.get_position(self.cm.get_indices()[0])
            pos.x += direction[0]
            pos.y += direction[1]

            if keyboard.Key.esc in pressed_keys:
                raise KeyboardInterrupt

        def input(self):
            pass


    # ________init_________

    input_impl = InputApiImpl()
    render_impl = CustomRendererImpl()

    engine = Engine(render_impl, input_impl, component_manager)
    try:
        engine.run()
    except KeyboardInterrupt:
        print("Game exited")
