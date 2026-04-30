import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
from sympy import *
import linalg as lin

t = [0,2*np.pi]
h = np.array([(t[1]-t[0])/n for n in  range(100,1000,100)])
print(len(h))
y0 = [0, 1]
def func(y, z, t):
    return z, -y
funzione_analitica = lambda x: np.sin(x)
derivata_analitica = lambda x: np.cos(x)
errori = []
for hi in h :
    equaz = lin.equazioni_differenziali(t, func, y0, hi)
    tempi, soluz = equaz.rk2()
    print(tempi[-1])
    valore_vero = derivata_analitica(t[-1])
    residuo = np.abs(soluz[1][-1]-valore_vero)
    errori.append(residuo)

errori = np.array(errori)
errori_1 = []
for hi in h :
    equaz = lin.equazioni_differenziali(t, func, y0, hi)
    tempi, soluz = equaz.forward_euler()
    #print(tempi[-1])
    valore_vero = derivata_analitica(t[-1])
    residuo = np.abs(np.abs(soluz[1][-1])-valore_vero)
    errori_1.append(residuo)
    

errori = np.array(errori)
errori_1 = np.array(errori_1)

fig, ax = plt.subplots(nrows= 2, ncols=1)
ax[0].scatter(np.arange(len(errori)),errori, label = 'rk2')
ax[1].scatter(np.arange(len(errori)),errori_1, label = 'eulero')
for i in range(len(ax)):
    ax[i].set_yscale('log')
    ax[i].legend()
plt.tight_layout()
plt.savefig('errori_rk2.png')
plt.show()



