import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin
import sympy as sp 
import seaborn as sns
from math import *
sns.set_theme(style='darkgrid')

htagliato = 1
m = 1
L = 1
V0 = 10
k = lambda E: (2*m*(V0+E)/htagliato)**0.5
ksign = lambda E : ((-2*m*E/htagliato))**0.5

def feven_s(E):
    return k(E)*sp.tan(k(E)*L/2)-ksign(E)

def feven(E):
    return k(E)*np.tan(k(E)*L/2)-ksign(E)

def fodd_s(E):
    return k(E)*(1/sp.tan(k(E)*L/2))+ksign(E)

def fodd(E):
    return k(E)*(1/np.tan(k(E)*L/2))+ksign(E)

xs = sp.symbols('x')
feven_simb = feven_s(xs)
x_guess = -6
a = -8
b = -6
rootc = lin.root_functions(a,b,feven)
solci, history = lin.newton(x_guess, feven_simb, max_iter =100)
solci1, history1 = lin.newton(x_guess, feven, max_iter =100)
solci2, history2 = rootc.bisezione()
solci3, history3 = rootc.regula_falsi()
residui = np.abs(history-solci)
residui1 = np.abs(history1-solci1)
residui2 = np.abs(history2-solci2)
residui3 = np.abs(history3-solci3)
print(f'Soluzione con Newton vale:{solci}')
print(f'Soluzione con finite differences:{solci}')
x = np.linspace(-9.9, -0.1,100)
x1= np.linspace(-9.9,0,100)
y = feven(x)
y[np.abs(y) > 50] = np.nan
y1 = fodd(x)
y1[np.abs(y1)>50]= np.nan
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,8))
ax[0].scatter(np.arange(len(history)), history, color = 'black', label = 'andamento soluzioni ')
ax[1].scatter(np.arange(len(residui)),residui , color = 'green', label = 'andamento residui con Newton')
for i in range(len(ax)):
    ax[i].set_xlabel('$n$')
    ax[i].set_ylabel('$f$')
    #ax[i].set_yscale('log')
    ax[i].legend()
plt.show()

fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,8))
plt.title('con finite derivatives')
ax[0].scatter(np.arange(len(history1)), history1, color = 'black', label = 'andamento soluzioni ')
ax[1].scatter(np.arange(len(residui1)),residui1 , color = 'green', label = 'andamento residui con Newton')
for i in range(len(ax)):
    ax[i].set_xlabel('$n$')
    ax[i].set_ylabel('$f$')
    #ax[i].set_yscale('log')
    ax[i].legend()
plt.show()


fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,8))
plt.title('con bisection ')
ax[0].scatter(np.arange(len(history2)), residui2, color = 'black', label = 'andamento soluzioni ')
ax[1].scatter(np.arange(len(residui2)),feven(history2) , color = 'green', label = 'andamento residui con bisezione')
for i in range(len(ax)):
    ax[i].set_xlabel('$n$')
    ax[i].set_ylabel('$f$')
    ax[i].set_yscale('log')
    ax[i].legend()
plt.show()


fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,8))
plt.title('con regula falsi')
ax[0].scatter(np.arange(len(history3)), residui3, color = 'black', label = 'andamento soluzioni ')
ax[1].scatter(np.arange(len(residui3)),feven(history3) , color = 'green', label = 'andamento residui con regula falsi')
for i in range(len(ax)):
    ax[i].set_xlabel('$n$')
    ax[i].set_ylabel('$f$')
 #   ax[i].set_yscale('log')
    ax[i].legend()
plt.show()
