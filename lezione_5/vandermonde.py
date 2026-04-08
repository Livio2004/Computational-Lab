import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin 
k = []

for i in range(4,17):
    x = np.linspace(-1,1,i)
    A = np.vander(x,increasing=True)
    sistema = lin.linear_system(A)
    Q,R = sistema.QR_decomposition(A)
    k.append(np.abs(R[1,1]/R[i-1,i-1]))
k = np.array(k)
plt.figure(figsize=(10,6))
plt.scatter(np.arange(4,17),k, label='condition number')
plt.yscale('log')
plt.legend()
plt.show()