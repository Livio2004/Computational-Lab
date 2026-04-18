import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin
from sympy import *

func = lambda x: x**2
x0 = 0.8
sol, history = lin.newton(x0, func)
print(sol)
print(history)
residui = np.abs(sol-history )
fig, ax = plt.subplots(nrows=2, ncols =1, figsize =(12,8))
x = np.linspace (-5,5,200)
y = func(x)
ax[0].plot(x,y, color = 'black', label='funzione iniziale')
ax[0].scatter(sol,func(sol), color = 'blue', label=f'soluzione = {sol:.3f}')
ax[1].plot(np.arange(len(history)),residui, color = 'green', label='residui e andamento (spero)quadratico')
for i in range(2):
    ax[i].set_xlabel('$x$')
    ax[i].set_ylabel('$y$')
    ax[i].legend()

plt.show()
