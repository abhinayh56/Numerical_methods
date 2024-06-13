import math

class RK4:
    def __init__(self, h_, t_0, y_0, diff_fun_):
        self.h = h_
        self.t_n = t_0
        self.y_n = y_0
        self.diff_fun = diff_fun_

    def update(self):
        k1 = self.diff_fun(self.t_n, self.y_n)
        k2 = self.diff_fun(self.t_n + self.h / 2.0, self.y_n + self.h*k1 / 2.0)
        k3 = self.diff_fun(self.t_n + self.h / 2.0, self.y_n + self.h*k2 / 2.0)
        k4 = self.diff_fun(self.t_n + self.h, self.y_n + self.h*k3)

        self.y_n = self.y_n + (self.h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)

        self.t_n = self.t_n + self.h

        return self.y_n