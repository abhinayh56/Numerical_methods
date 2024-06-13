import math
import numpy as np
import euler as eul
import rk4 as rk4
import matplotlib.pyplot as plt

# Exact solution
T = 10
dt = 0.004
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

global I
I = 0.0

def model_1(t, X):
    # spring mass damper system
    m = 0.25
    k = 10.0
    c = 0.5
    F = 0.0

    X_1 = X[0]
    X_2 = X[1]

    dY_dt_1 = X_2
    dY_dt_2 = (1.0/m) * (F - k*X_1 -c*X_2)

    dY_dt = np.array([dY_dt_1, dY_dt_2])

    return dY_dt

# time stamp and initial condition for solving the IVP
dt = 0.01
N = int(T/dt)
t = np.linspace(0,T,N)
t_0 = 0.0
y_0 = np.array([0.0, 10.0])

# Solution using Euler method
int_1 = eul.Euler(dt, t_0, y_0, model_1)
y_1 = np.zeros((len(t), len(y_0)))
y_1[0,:] = y_0
for i in range(0, len(t)-1):
    y_1[i+1,:] = int_1.update()

x_1 = y_1[:,0]
dx_dt_1 = y_1[:,1]

# Solution using RK4 method
int_2 = rk4.RK4(dt, t_0, y_0, model_1)
y_2 = np.zeros((len(t), len(y_0)))
y_2[0,:] = y_0
for i in range(0, len(t)-1):
    y_2[i+1,:] = int_2.update()

x_2 = y_2[:,0]
dx_dt_2 = y_2[:,1]

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t,x_1,'r:',linewidth=4)
plt.plot(t,x_2,'y-',linewidth=2)
plt.title("Position")
plt.xlabel('t (s)')
plt.ylabel('y')
plt.legend(["Euler",'RK4'])
plt.grid()

plt.subplot(2,1,2)
plt.plot(t,dx_dt_1,'r:',linewidth=4)
plt.plot(t,dx_dt_2,'y-',linewidth=2)
plt.title("Velocity")
plt.xlabel('t (s)')
plt.ylabel('dy_dt')
plt.legend(["Euler",'RK4'])
plt.grid()

plt.show()
