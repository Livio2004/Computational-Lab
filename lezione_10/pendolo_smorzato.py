import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
from sympy import *
import linalg as lin

t = [0,2*np.pi]
h = 0.1
y0 = [0, 1]
A = 0
gamma = 0.3
def func(theta, omega, t):
    gamma = 0.9 
    A = 0
    d_theta = omega
    d_omega = -np.sin(theta) - gamma * omega + A * np.sin(2/3 * t)
    
    return [d_theta, d_omega]

funzione_analitica = lambda x: np.sin(x)
equaz = lin.equazioni_differenziali(t, func, y0, h)
tempi, soluz = equaz.forward_euler()
tempi_rk2, soluz_rk2 = equaz.rk2()
#print(tempi_rk2)
#print(soluz_rk2)

x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (12,8))
ax[0].plot(x, funzione_analitica(x), label = 'funzione analitica')
ax[0].plot(tempi,soluz[0], label = 'metodo eulero')
ax[0].plot(tempi_rk2,soluz_rk2[0], label = 'metodo rk2')
ax[1].scatter(soluz[0], soluz[1], label = 'spazio fasi')
ax[1].scatter(soluz_rk2[0], soluz_rk2[1], label = 'spazio fasi rk2')
for i in range(len(ax)):
    ax[i].set_xlabel('x')
    ax[i].set_ylabel('y')
    ax[i].legend()

plt.tight_layout()
plt.show()