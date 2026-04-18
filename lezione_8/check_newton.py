import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin
from sympy import *
import seaborn as sns
sns.set_theme(style='darkgrid')


func = lambda x: x**3-2*x**2-11*x+12
x0 = 2.352837350
x01 = 2.352836327
x0try=2.352836323 
sol1, history1 = lin.newton(x0, func)
sol2, history2 = lin.newton(x01, func)
sol, history = lin.newton(x0try, func)

fig, ax = plt.subplots(nrows=1, ncols =4, figsize =(14,8))
x = np.linspace (-5,5,200)
y = func(x)
ax[0].plot(x,y, color = 'black', label='funzione iniziale')
ax[1].scatter(np.arange(len(history1)),history1, color = 'blue', label=f'andamento con x0 = {x0}\n sol = {sol1}')
ax[2].scatter(np.arange(len(history2)),history2, color = 'purple', label=f'andamento con x0 = {x01}\n sol = {sol2}')
ax[3].scatter(np.arange(len(history)), history, color = 'grey', label =f'andamento con x0={x0try}\n sol = {sol}')

for i in range(len(ax)):
    ax[i].set_xlabel('$x$')
    ax[i].set_ylabel('$y$')
    ax[i].legend()

plt.tight_layout()
plt.show()
