import math
from wisayoengine.core import Vector

class Transform:
    def __init__(self,
        x_axis=Vector(1., 0.),
        y_axis=Vector(0., 1.),
        origin=Vector(0, 0)
    ):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.origin = origin

    def get_translated(self, offset):
        return Transform(self.x_axis, self.y_axis, offset)

    @staticmethod
    def get_scaled(scale):
        x_ax = Vector(scale.x, 0)
        y_ax = Vector(0, scale.y)
        return Transform(x_ax, y_ax)

    @staticmethod
    def get_rotated(angle):
        x_ax = Vector(math.cos(angle), -math.sin(angle))
        y_ax = Vector(math.sin(angle), math.cos(angle))
        return Transform(x_ax, y_ax)

    def __mul__(self, other):
        x_axis = Vector(self.x_axis.x * other.x_axis.x + self.x_axis.y * other.y_axis.x,
                        self.x_axis.x * other.x_axis.y + self.x_axis.y * other.y_axis.y)
        y_axis = Vector(self.y_axis.x * other.x_axis.x + self.y_axis.y * other.y_axis.x,
                        self.y_axis.x * other.x_axis.y + self.y_axis.y * other.y_axis.y)
        origin = Vector(self.origin.x * other.origin.x + self.origin.y * other.origin.x,
                        self.origin.x * other.origin.y + self.origin.y * other.origin.y)
        return Transform(x_axis,y_axis,origin)


    # def __repr__(self):
    #     return (f"{self.x_axis.x} {self.x_axis.y}\n"
    #             f"{self.y_axis.x} {self.y_axis.y}\n")

