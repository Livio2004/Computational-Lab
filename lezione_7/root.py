import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit
import linalg as lin

func = lambda x: 0.5 + x -x**2
a = 0   
b = 2
soluzioni = lin.root_functions(a, b, func)
rootf, root =  soluzioni.bisezione()
print(soluzioni.a, soluzioni.b)
rootf1, root1 =  soluzioni.regula_falsi()
print(soluzioni.a, soluzioni.b)
print('la soluzione vale ', func(rootf))
print('Il numero di iterazioni con bisezione',len(root))
print('Il numero previsto di ripe con bisezione è :',soluzioni.controllo_iterazioni_bisezione())
print('Il numero di iterazioni con regula falsi',len(root1))

n = np.arange(len(root))
n1 = np.arange(len(root1))
fc= np.abs(func(root))
fc1 = np.abs(func(root1))
diff = np.abs(rootf-root)
diff1 = np.abs(rootf1-root1)

fig, ax = plt.subplots(nrows=2, ncols = 1)
ax[0].scatter(n,fc,color = 'blue', label = 'scatter andamento soluzioni con bisezione')
ax[0].scatter(n1,fc1,color = 'green', label = 'scatter andamento soluzioni con regula falsi')
ax[0].legend()
ax[0].set_title('soluzioni')
ax[1].set_title('residui')
ax[1].scatter(n,diff,color = 'blue', label = 'residui con bisezione')
ax[1].scatter(n1,diff1,color = 'green', label = 'residui con regula falsi')
ax[1].legend()
for i in range(len(ax)):
    ax[i].set_xlabel('numero di iteraizoni')
    ax[i].set_ylabel('andamento')
    ax[i].set_yscale('log')
plt.tight_layout()
plt.show()


