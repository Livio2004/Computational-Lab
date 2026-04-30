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

equaz = lin.equazioni_differenziali(t, func, y0, h)
tempi, soluz = equaz.forward_euler()
plt.scatter(soluz[0], soluz[1])
plt.show()


func = lambda y, x : x*y
risultato_analitico = lambda x: 2*np.exp((x**2)/2)
y0 = 2
h =[0.1,0.01]
xi = np.array([0,1])
risultati={}
for hi in h:
    equaz1 = lin.equazioni_differenziali(xi, func, y0, hi)
    t_sol, y_sol = equaz1.forward_euler()
    risultati[hi] = {"t": t_sol, "y": y_sol}
x = risultati[h[0]]['t']
plt.figure(figsize=(12,6))
for hi, data in risultati.items():
    plt.scatter(data["t"], data["y"], label=f'h = {hi}')
plt.plot(x, risultato_analitico(x), ls = '--', label = 'funzione analitica')
plt.legend()
plt.show()



