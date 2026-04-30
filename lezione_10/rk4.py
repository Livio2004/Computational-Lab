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
tempi, soluz = equaz.forward_euler()
tempi_rk2, soluz_rk2 = equaz.rk4()
#print(tempi_rk2)
#print(soluz_rk2)

x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (12,8))
ax[0].plot(x, funzione_analitica(x), label = 'funzione analitica')
ax[0].plot(tempi,soluz[0], label = 'metodo eulero')
ax[0].plot(tempi_rk2,soluz_rk2[0], label = 'metodo rk4')
ax[0].plot(tempi, soluz[1], label = 'eulero derivata prima')
ax[1].scatter(soluz[0], soluz[1], label = 'spazio fasi')
ax[1].scatter(soluz_rk2[0], soluz_rk2[1], label = 'spazio fasi rk4')
for i in range(len(ax)):
    ax[i].set_xlabel('x')
    ax[i].set_ylabel('y')
    ax[i].legend()

plt.tight_layout()
plt.show()

t = [0,2*np.pi]
h = [(t[1]-t[0])/n for n in  range(100,1000,100)]
y0 = [0, 1]
def func(y, z, t):
    return z, -y
funzione_analitica = lambda x: np.sin(x)
derivata_analitica = lambda x: np.cos(x)
errori = []
for hi in h :
    equaz = lin.equazioni_differenziali(t, func, y0, hi)
    tempi, soluz = equaz.rk4()
    print(tempi[-1])
    valore_vero = derivata_analitica(t[-1])
    residuo = np.abs(np.abs(soluz[1][-1])-valore_vero)
    errori.append(residuo)

errori = np.array(errori)

plt.scatter(np.arange(len(errori)), errori)
plt.yscale('log')
plt.show()


