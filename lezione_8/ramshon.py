import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin
from sympy import *
import seaborn as sns
sns.set_theme(style='darkgrid')

func = lambda x: x**3-2*x+2
x0 = 0
x01 = 1
x0try= 3
sol1, history1 = lin.newton(x0, func)
sol2, history2 = lin.newton(x01, func)
sol, history = lin.newton(x0try, func)
plt.scatter(np.arange(len(history)), history)
plt.show()

fig, ax = plt.subplots(nrows=1, ncols =3, figsize =(14,8))
x = np.linspace (-5,5,200)
y = func(x)
ax[0].plot(x,y, color = 'black', label='funzione iniziale')
ax[1].scatter(np.arange(len(history1)),history1, color = 'blue', label=f'andamento con x0 = {x0}')
ax[2].scatter(np.arange(len(history2)),history2, color = 'purple', label=f'andamento con x0 = {x01}')
for i in range(3):
    ax[i].set_xlabel('$x$')
    ax[i].set_ylabel('$y$')
    ax[i].legend()

plt.show()
