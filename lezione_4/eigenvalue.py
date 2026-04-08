import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
import linalg as lin

#bisogna usare alg di tipo operativo per Abel-Ruffini perchè convergono ad infinito

#la logica è che io salvo y come Ay e itero

def power_method(A,n):
    s = A.shape[0]
    y = np.random.randn(s)+ 1j*(np.random.randn(s))
    y /= np.sqrt(np.real(y.conj().T@y))
    residuo = 10
    ls = []
    for i in range(n):
        if residuo >(10**(-8)):
            y = A@y
            y /= np.sqrt(np.real(y.conj().T@y))
            fase = y[0]/np.abs(y[0])
            y = y/fase
            ls.append((y.conj().T @A@y)/np.sqrt(np.real(y.conj().T@y)))
            if i >0:
                residuo = np.abs(ls[i]-ls[i-1])
        else :
            print(f'precisione raggiunta a interazione {i}')
            break
    ls = ls[-1]
    return ls, y



A = np.array([[4.0,-1.0j,2],
               [1j,2,2+7j],
                 [2, 2-7j, -2]])
b = np.array([1.0,2,7])
n = 1000 #max numero di iterazioni
ls, autovettore = power_method(A,n)
print(ls)
print(autovettore)
print(A@autovettore)
print(ls*autovettore)
sistema = lin.linear_system(A)
autovalori, autovettori= sistema.eigensolver_QR(10**(-10), 10000)
print(f'gli autovalori sono {autovalori}')
print(f'gli autovettori sono {autovettori}')


'''plt.figure(figsize=(10,6))
plt.plot(residui)
plt.xlabel('numero iterazioni')
plt.ylabel('residuo power method')
plt.yscale('log')
plt.show()
'''