import lexem
import vec

_LEXEM_OBJ = 'lexemObj'

class LexemObj(lexem.Lexem):
    def __init__(self):
        super().__init__()
        self.name = _LEXEM_OBJ
        self.pos = vec.Vec(0, 0)