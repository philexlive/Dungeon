from lib.physics import Velocity

class PhyObj:
    def __init__(self, 
                 mesh=None, 
                 colbox=None, 
                 pos_x=0, 
                 pos_y=0, 
                 velocity=Velocity(0, 0), 
                 inherit=True
                 ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mesh = mesh
        self.colbox = colbox
        self.velocity = velocity
        self.inherit = inherit
