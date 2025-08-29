class InputSystem:
    def __init__(self, input_api):
        self.input_api = input_api

    def initialize_input(self):
        self.input_api.on_input()

    def handle_input(self):
        self.input_api.on_input()
