import lexemobj

_LEXEM_SPRITE = 'lexemSprite'

class LexemSprite(lexemobj.LexemObj):
    def __init__(self):
        super().__init__()
        self.name = _LEXEM_SPRITE
        self.tex = None