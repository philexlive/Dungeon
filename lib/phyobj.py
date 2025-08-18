class PhyObj:
    def __init__(self, mesh, colbox, pos_x, pos_y, velocity, inherit):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mesh = mesh
        self.colbox = colbox
        self.velocity = velocity
        self.inherit = inherit
