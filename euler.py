import math

class Euler:
    def __init__(self, h_, t_0, y_0, diff_fun_):
        self.h = h_
        self.t_n = t_0
        self.y_n = y_0
        self.diff_fun = diff_fun_

    def update(self):
        self.y_n = self.y_n + self.h*self.diff_fun(self.t_n, self.y_n)
        self.t_n = self.t_n + self.h

        return self.y_n