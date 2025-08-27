import lexemobj


_LEXEM_CAM = 'lexemCam'

class LexemCam(lexemobj.LexemObj):
    def __init__(self):
        super().__init__()
        self.name = _LEXEM_CAM
        self.dead_zone_enabled = False
        self.dead_zone = utilobjs.Box(0, 0, 1, 1)