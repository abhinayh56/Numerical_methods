import math
import numpy as np
import euler as eul
import rk4 as rk4
import matplotlib.pyplot as plt

# Exact solution
T = 10
dt = 0.001
N = int(T/dt)
t_exact = np.linspace(0,T,N)

A = 10.0
f = 1.0 / 1
w = 2.0*np.pi*f
y_exact = A*np.sin(w*t_exact)

# differential equation
def diff_fun(x, y):
    A = 10.0
    T = 1.0
    f = 1.0 / T
    w = 2.0*math.pi*f

    return A*w*math.cos(w*x)

# time stamp and initial condition for solving the IVP
dt = 0.05
N = int(T/dt)
t = np.linspace(0,T,N)
t_0 = 0.0
y_0 = 0.0

# Solution using Euler method
int_1 = eul.Euler(dt, t_0, y_0, diff_fun)
y_1 = np.zeros(len(t))
for i in range(0, len(t)-1):
    y_1[i+1] = int_1.update()

# Solution using RK4 method
int_2 = rk4.RK4(dt, t_0, y_0, diff_fun)
y_2 = np.zeros(len(t))
for i in range(0, len(t)-1):
    y_2[i+1] = int_2.update()


plt.figure(1)
plt.plot(t_exact,y_exact, 'k-',linewidth=4)
plt.plot(t,y_1,'r:',linewidth=4)
plt.plot(t,y_2,'y-',linewidth=2)
plt.title("ODE solver")
plt.xlabel('t (s)')
plt.ylabel('y')
plt.legend(["Exact", "Euler",'RK4'])
plt.grid()
plt.show()