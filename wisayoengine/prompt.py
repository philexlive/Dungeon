class PromptState:
    def __init__(self, style):
        self.style = style

_prompt = PromptState("Y->==>")

def change_prompt(new):
    """Change prompt style.

    :param new: str - a new prompt pattern.

    Saves prompt style in global prompt's state.
    """
    _prompt.style = new

def action():
    """Get input with stylized prompt.
    """
    return input(_prompt.style)
