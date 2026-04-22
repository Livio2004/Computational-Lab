import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
from sympy import *
import linalg as lin

n = 6
H, coeff, Hnumpy = lin.Hermite(n) #polinomio di Hermite grado 6
print(f'Il polinomio di hermite è {H}')
print(coeff)
print('\nCalcolo companion matrix...')

C = np.eye(n, k = 1)
C[-1,:]= -1*coeff[0:n]/coeff[-1]
print('La companion matrix vale\n',C)

s = 10.0
C_shifted = C + (s * np.eye(6))

eig = lin.linear_system(C_shifted)
print('Calcolo zeri con QR eigensolver...\n')
autovalori, autovettori, _ = eig.eigensolver_QR(100000)
autovalori = autovalori - s
print(autovalori,'\n')
x = np.linspace(-2.5,2.5,1000)
y = Hnumpy(x)
plt.figure(figsize = (12,6))
plt.scatter(autovalori, Hnumpy(autovalori), color = 'red', label='zeri con QR')
plt.plot(x,y, label = f'polinomio {H}')
plt.axhline(0,ls = '--')
plt.tight_layout()
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

eig.residui_QR(1000)