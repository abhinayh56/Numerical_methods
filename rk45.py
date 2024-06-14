import numpy as np

class RK45:
    def __init__(self, h_, t_0, y_0, diff_fun_):
        self.h = h_
        self.t_n = t_0
        self.y_n = y_0
        self.diff_fun = diff_fun_
        self.e_tol = 1e-15
        self.beta = 1.0

    def update(self):
        k1 = self.h*self.diff_fun(self.t_n, self.y_n)
        k2 = self.h*self.diff_fun(self.t_n + self.h * (1.0/4.0)  , self.y_n + (1.0/4.0      )*k1)
        k3 = self.h*self.diff_fun(self.t_n + self.h * (3.0/8.0)  , self.y_n + (3.0/32.0     )*k1 + (9.0/32.0      )*k2)
        k4 = self.h*self.diff_fun(self.t_n + self.h * (12.0/13.0), self.y_n + (1932.0/2197.0)*k1 + (-7200.0/2197.0)*k2 + (7296.0/2197.0 )*k3)
        k5 = self.h*self.diff_fun(self.t_n + self.h * (1.0)      , self.y_n + (439.0/216.0  )*k1 + (-8.0          )*k2 + (3680.0/513.0  )*k3 + (-845.0/4104.0)*k4)
        k6 = self.h*self.diff_fun(self.t_n + self.h * (1.0/2.0)  , self.y_n + (-8.0/27.0    )*k1 + (2.0           )*k2 + (-3544.0/2565.0)*k3 + (1859.0/4104.0)*k4 + (-11.0/40.0)*k5)

        y_n_4 = self.y_n + (25.0/216.0)*k1 + (1408.0/2565.0)*k3 + (2197.0/4104.0)*k4 -  (1.0/5.0)*k5
        y_n_5 = self.y_n + (16.0/135.0)*k1 + (6656.0/12825.0)*k3 + (28561.0/56430.0)*k4 +  (-9.0/50.0)*k5 +  (2.0/55.0)*k6

        self.y_n = y_n_5
        
        e = np.linalg.norm(y_n_5 - y_n_4)
        
        print(e, self.e_tol/e, self.h, e>=self.e_tol)

        # if(e>=self.e_tol):
            # self.h = self.beta*self.h*(self.e_tol/e)**0.2
            # self.update()
        # else:
            # self.h = self.beta*self.h*(self.e_tol/e)**0.25
            # self.h = self.h
        
        self.t_n = self.t_n + self.h

        return self.y_n