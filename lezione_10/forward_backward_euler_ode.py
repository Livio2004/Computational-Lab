import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
from sympy import *
import linalg as lin

func = lambda x, y : x*y
risultato_analitico = lambda x: 2*np.exp((x**2)/2)
y0 = 2
h =[0.1,0.01]
xi = np.array([0,1])
risultati={}
for hi in h:
    t_sol, y_sol = lin.forward_euler(xi, func, y0, hi)
    risultati[hi] = {"t": t_sol, "y": y_sol}
x = risultati[h[0]]['t']
plt.figure(figsize=(12,6))
for hi, data in risultati.items():
    plt.scatter(data["t"], data["y"], label=f'h = {hi}')
plt.plot(x, risultato_analitico(x), ls = '--', label = 'funzione analitica')
plt.legend()
plt.show()

'''
t_soll, y_soll  = lin.backward_euler(xi, func, y0, h[0])
plt.plot(t_soll, y_soll)
plt.show()
'''


risultati1 = {}
for hi in h:
    t_sol1, y_sol1 = lin.backward_euler(xi, func,y0,hi)
    risultati1[hi] = {"t": t_sol1, "y":y_sol1}

x = risultati1[h[0]]['t']
for h, data in risultati1.items():
    plt.scatter(data['t'], data['y'], label=f'h = {h}')    
plt.plot(x, risultato_analitico(x), ls = '--', label = 'funzione analitica')
plt.legend()
plt.show()

