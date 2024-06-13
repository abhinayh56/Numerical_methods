import math

class Euler:
    def __init__(self, h_, t_0, y_0):
        self.h = h_
        self.t_n = t_0
        self.y_n = y_0

    def update(self):
        A = 10.0
        T = 1.0
        f = 1.0 / T
        w = 2.0*math.pi*f
        self.y_n = self.y_n + self.h*A*w*math.cos(w*self.t_n)
        self.t_n = self.t_n + self.h

        return self.y_n