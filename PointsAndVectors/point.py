import math

from geom2d.vector import Vector
from geom2d.vector import Vector

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
    def __sub__(self,other):
        return Point(
            self.x - other.x,
            self.y - other.y
        )



    def displaced(self,vector: Vector, times = 1):
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v
        )

p = Point(2,3)
v = Vector(10,20)
p_prime = p.displaced(v, 2)
print(p_prime.__dict__)