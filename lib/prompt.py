class PromptState:
    def __init__(self, style):
        self.style = style

_prompt = PromptState("Y->==>")

def change_prompt(new):
    _prompt.style = new

def action():
    return input(_prompt.style)
