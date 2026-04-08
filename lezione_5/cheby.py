import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 

runge = lambda x: 1/(1+25*x**2)
n_values = np.arange(10,41,10)
x_sample= np.linspace(-1,1,1000)
plt.figure(figsize = (10,6))
for i in n_values:
    x = []
    x1 = np.linspace(-1,1,i)
    for j in range(i):
        xj = -1*np.cos(j*np.pi/(i-1))
        x.append(xj)
    x = np.array(x)
    y = runge(x)
    y1 = runge(x1)
    pol = lin.interpolazioni(x,y)
    polv = pol.lagrange_interpolation(x_sample)
    pol1 = lin.interpolazioni(x1,y1)
    polv1 = pol1.lagrange_interpolation(x_sample)
    plt.scatter(x,y)
    plt.plot(x_sample, polv)
    plt.fill_between(x_sample, polv1,alpha=0.1)
plt.ylim(0,3)
plt.show()
    
    

