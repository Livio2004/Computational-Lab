import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin

def exponential(x, R):
    return np.exp(-R*(x-0.5)**2)


L = 1.0
N = 50
R1 = 10
R2 = 100

x = np.arange(0, N)/N
rho1 = exponential(x, R1)
rho2 = exponential(x,R2)
K = 2*np.eye(N)-np.eye(N, k=1)-np.eye(N, k=-1)

sistema1 = lin.linear_system(K, rho1)
sistema2 = lin.linear_system(K, rho2)
soluzione1 = sistema1.solve()
soluzione2 = sistema2.solve()

plt.figure(figsize = (10,6))
plt.plot(x, soluzione1, label = 'R = 10')
plt.plot(x, soluzione2, label = 'R=100')
plt.legend()
plt.xlabel('x/L')
plt.ylabel('densità di carica')
plt.show()