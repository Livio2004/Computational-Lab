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
def func(y, z, t):
    return z, -y
funzione_analitica = lambda x: np.sin(x)
equaz = lin.equazioni_differenziali(t, func, y0, h)
tempi, soluz = equaz.symplectic_euler()
tempi_rk2, soluz_rk2 = equaz.forward_euler()
print(soluz)
#print(soluz_rk2)

x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (12,8))
ax[0].plot(x, funzione_analitica(x), label = 'funzione analitica')
ax[0].plot(tempi,soluz[0], label = 'metodo simplettico')
ax[0].plot(tempi_rk2,soluz_rk2[0], label = 'metodo rk2')
ax[0].plot(tempi, soluz[1], label = 'eulero derivata prima')
ax[1].scatter(soluz[0], soluz[1], label = 'spazio fasi')
ax[1].scatter(soluz_rk2[0], soluz_rk2[1], label = 'spazio fasi rk2')
for i in range(len(ax)):
    ax[i].set_xlabel('x')
    ax[i].set_ylabel('y')
    ax[i].legend()

plt.tight_layout()
plt.show()
